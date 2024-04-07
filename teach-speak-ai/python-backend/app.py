from flask import Flask
from Recorder import Recorder

app = Flask(__name__)
recorder = Recorder()

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/api/start_recording')
def start_recording_api():
    recorder.start_recording()
    return "Recording started."

@app.route('/api/stop_recording')
def stop_recording_api():
    recorder.stop_recording()
    return "Recording stopped."

if __name__ == '__main__':
    app.run(port=5000)
