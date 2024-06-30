from flask import Flask
from recorder import Recorder, get_audio_devices
from flask_cors import CORS
import time
from count_keywords import count_keywords

app = Flask(__name__)
recorder = Recorder()
CORS(app)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/api/start_recording')
def start_recording_api():
    recorder.start_recording()
    return "Recording started successfully"

@app.route('/api/stop_recording')
def stop_recording_api():
    recorder.stop_recording()
    return recorder.get_path()

@app.route('/api/submit-audio')
def submit_audio_api():
    text = recorder.submit_audio()
    keyword_counts = count_keywords(text) 
    return keyword_counts

@app.route('/api/get_audio_drivers')
def get_audio_api():
    return get_audio_devices()

@app.route('/api/set_driver/<driver>', methods=['POST'])
def set_audio_api(driver):
    recorder.set_audio_device(driver)
    return get_audio_devices()

if __name__ == '__main__':
    app.run(port=5000)
