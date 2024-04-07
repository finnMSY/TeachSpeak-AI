import sounddevice as sd
import soundfile as sf
import time
import keyboard
import concurrent.futures
from datetime import datetime
import os

def get_default_audio_device():
    default_input_device_info = sd.query_devices(device=sd.default.device[0])
    return default_input_device_info

class Recorder:
    def __init__(self, samplerate=44100, channels=2, duration=10, device=get_default_audio_device()['name']):
        self.samplerate = samplerate
        self.channels = channels
        self.recording = False
        self.input_device = device
        self.max_duration = duration
        self.stop_flag = False

    def start_recording(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Start recording in a separate thread
            future = executor.submit(self._record)  # Removed unnecessary arguments
            
            # Run your main loop
            start_time = time.time()
            # while time.time() - start_time < self.max_duration:
            #     if self.stop_flag:
            #         break

            while True:
                if keyboard.is_pressed('enter'):
                    self.stop_recording()
                    break
            
            print("Hello")

            # Wait for the recording to finish and get the result
            audio_data = future.result()

            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
            output_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio_files")
            filename = os.path.join(output_directory, f"{current_time}-recording.wav")

            sf.write(filename, audio_data, self.samplerate)

    def stop_recording(self):
        self.stop_flag = True  # Use self.stop_flag

    def _record(self):
        # Record audio
        print("Recording: press ENTER to stop")
        recording = sd.rec(int(self.max_duration * self.samplerate), samplerate=self.samplerate, channels=self.channels, device=self.input_device, dtype='int16')
        
        # Start time for checking duration
        start_time = time.time()

        # Check for duration completion
        while time.time() - start_time < self.max_duration:
            if self.stop_flag:
                print("Recording stopped.")
                break
            time.sleep(0.1)  # Adjust sleep time as needed to avoid high CPU usage
        
        # Stop recording
        sd.stop()

        # Get the recorded audio data up to the point where 'x' was pressed
        recorded_audio = recording[:int((time.time() - start_time) * self.samplerate)]

        print("Recording completed.")
        return recorded_audio

r = Recorder(device=get_default_audio_device()['name'])
r.start_recording()

time.sleep(3)
r.stop_recording()