from flask import Flask
from Recorder import Recorder
from flask_cors import CORS

app = Flask(__name__)
recorder = Recorder()
CORS(app)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/api/start_recording')
def start_recording_api():
    recorder.start_recording()

@app.route('/api/stop_recording')
def stop_recording_api():
    recorder.stop_recording()

if __name__ == '__main__':
    app.run(port=5000)
