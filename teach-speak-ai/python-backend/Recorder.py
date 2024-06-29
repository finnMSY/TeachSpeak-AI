import sounddevice as sd
import soundfile as sf
import time
import concurrent.futures
from datetime import datetime
import os
from aws import transcribe_audio, upload_to_s3

# Gets the computer's audio devices
def get_audio_devices() -> list:
    default_input_device_info = dict(sd.query_devices(device=sd.default.device[0]))
    return [sd.query_devices(), default_input_device_info]

class Recorder:
    def __init__(self, samplerate=44100, channels=2, duration=10, device=None):
        self.samplerate = samplerate
        self.channels = channels
        self.recording = False
        self.input_device = device or get_audio_devices()[1]['name']
        self.max_duration = duration
        self.stop_flag = False
        self.path = None

    def set_audio_device(self, device):
        self.input_device = device

    @staticmethod
    def get_current_time():
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        return current_time

    # Starts the recording in a thread so that it checks for the stop_recording() at the same time
    def start_recording(self):
        self.stop_flag = False
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self._record)

    # When this function is called it stops the recording
    def stop_recording(self):
        self.stop_flag = True

    def get_path(self):
        return str(self.path)

    # Submits the audio file for transcription
    def submit_audio(self):
        transcription_output_directory = "transcribed_audio_files"
        os.makedirs(transcription_output_directory, exist_ok=True)
        file_name = self.path.split("\\")[-1]
        upload_to_s3(file_name=self.path, bucket="teachspeak", object_name=f"transcribed-audio-files/{file_name}")
        transcribe_audio(self.path, os.path.join(transcription_output_directory, f"{self.get_current_time()}-transcription.txt"))

    # Logic method that is run parallel to the stop_recording() checks
    def _record(self):
        print("Recording...")
        
        # Starts the recording
        try:
            recording = sd.rec(int(self.max_duration * self.samplerate), samplerate=self.samplerate, channels=self.channels, device=1, dtype='int16')
        except Exception as e:
            print(e)
        print("HELLO")
        
        # Checks for whether the max_duration is up, or the stop_recording() has been triggered
        start_time = time.time()
        while time.time() - start_time < self.max_duration and not self.stop_flag:
            # This basically means if the conditions aren't met do nothing
            time.sleep(0.1)

        # Once one of these events have been triggered, stop the recording
        sd.stop()

        # Store the audio file
        recorded_audio = recording[:int((time.time() - start_time) * self.samplerate)]

        print("Recording completed.")

        # Generate the audio file name
        output_directory = "audio_files"
        os.makedirs(output_directory, exist_ok=True)
        filename = os.path.join(output_directory, f"{self.get_current_time()}-recording.wav")

        # Set the stopping event to false so it can be repeated if wished to
        self.stop_flag = False

        # Writes the audio file to local storage
        self.path = filename
        sf.write(filename, recorded_audio, self.samplerate)