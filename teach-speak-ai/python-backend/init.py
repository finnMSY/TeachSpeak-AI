from flask import Flask
from Recorder import Recorder

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/api/start_recording')
def get_data():
    Recorder.start_recording()

@app.route('/api/stop_recording')
def get_data():
    Recorder.stop_recording()
    
if __name__ == '__main__':
    app.run(debug=True)
