import React, { useState } from 'react';
import './home-page.css';
import axios from "axios";

function HomePage() {
    const [recording, setRecording] = useState(false);

    const startRecording = async () => {
        try {
            setRecording('loading');
            const response = await axios.get("http://localhost:5000/api/start_recording");
            console.log(response.data)
            setRecording(true);
        } catch (error) {
            console.error("Error starting recording:", error);
            setRecording(false);
        }
    }

    const stopRecording = async () => {
        try {
            const response = await axios.get("http://localhost:5000/api/stop_recording");
            console.log(response.data); // Assuming the response contains the path to the saved audio file
            setRecording("saved")
            setRecording(false);
        } catch (error) {
            console.error("Error stopping recording:", error);
        }
    }

    return (
        <div>
            <h1>Recording Page</h1>
            <button onClick={startRecording}>Start</button>
            <button onClick={stopRecording}>Stop</button>

            {recording === 'loading' && 
                <p>Recording...</p>
            }
        </div>
    );
}

export default HomePage;
