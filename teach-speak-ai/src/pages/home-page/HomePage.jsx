import React, { useEffect, useState, useContext} from 'react';
import RootContext from "../../providers/root";
import './home-page.css';
import axios from "axios";

function HomePage() {
    const {
        setCurrentPage
      } = useContext(RootContext);

    const [recording, setRecording] = useState(false);
    const [driversList, setDriversList] = useState([]);
    const [defaultDriver, setDefaultDriver] = useState({});

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

    const getAudioDrivers = async () => {
        try {
            const response = await axios.get("http://localhost:5000/api/get_audio_drivers");
            const driverList = response.data[0];
            const defaultDriver = response.data[1];
            setDriversList(driverList);
            setDefaultDriver(defaultDriver);
        } catch (error) {
            console.error("Error, couldn't retrieve drivers:", error);
        }
    }

    const setCurrentDriver = async (driver) => {
        try {
            const response = await axios.post(
                `http://localhost:5000/api/set_driver/${driver}`,
                {
                    headers: {
                    "Content-Type": "multipart/form-data",
                    },
                }
            );
        } catch (error) {
            console.error("Error, couldn't set driver:", error);
        }
    }

    useEffect(() => {
        getAudioDrivers();  
    }, []);

    return (
        <div>
            <h1>Recording Page</h1>
            <select onChange={(e) => setCurrentDriver(e.target.value)}>
                <option value={defaultDriver.name}>{defaultDriver.name}</option>
                {driversList.map((option, index) => (
                    option.name !== defaultDriver.name && (
                        <option key={index} value={option.name}>{option.name}</option>
                    )
                ))}
            </select>
            <button onClick={startRecording}>Start</button>
            <button onClick={stopRecording}>Stop</button>
            <button onClick={() => setCurrentPage("loading")}>Next Page</button>


            {recording === 'loading' && 
                <p>Recording...</p>
            }
        </div>
    );
}

export default HomePage;
