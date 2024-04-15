import sounddevice as sd
import soundfile as sf
import time
import concurrent.futures
from datetime import datetime
import os

# Gets the computers default audio device
def get_default_audio_device():
    default_input_device_info = sd.query_devices(device=sd.default.device[0])
    return default_input_device_info

# Returns a list of all the computers connected audio devices
def get_all_audio_devices():
    return sd.query_devices()

class Recorder:
    def __init__(self, samplerate=44100, channels=2, duration=10, device=get_default_audio_device()['name']):
        self.samplerate = samplerate
        self.channels = channels
        self.recording = False
        self.input_device = device
        self.max_duration = duration
        self.stop_flag = False
        self.path = None

    # Starts the recording in a thread so that it checks for the stop_recording() at the same time
    def start_recording(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self._record)

    # When this function is called it stops the recording
    def stop_recording(self):
        self.stop_flag = True

    # Logic method that is run parallel to the stop_recording() checks
    def _record(self):
        print("Recording...")

        # Starts the recording
        recording = sd.rec(int(self.max_duration * self.samplerate), samplerate=self.samplerate, channels=self.channels, device=self.input_device, dtype='int16')
        
        # Checks for whether the max_duration is up, or the stop_recording() has been triggered
        start_time = time.time()
        while time.time() - start_time < self.max_duration and not self.stop_flag:
            # This bascially means if the conditions aren't met do nothing
            time.sleep(0.1)

        # Once one of these events have been triggered, stop the recording
        sd.stop()

        # Store the audio file
        recorded_audio = recording[:int((time.time() - start_time) * self.samplerate)]

        print("Recording completed.")

        # Generate the audio file name
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        output_directory = "audio_files"
        filename = os.path.join(output_directory, f"{current_time}-recording.wav")

        # Set the stopping event to false so it can be repeated if wished to
        self.stop_flag = False

        # Writes the audio file to local storage
        self.path = filename
        sf.write(filename, recorded_audio, self.samplerate)
