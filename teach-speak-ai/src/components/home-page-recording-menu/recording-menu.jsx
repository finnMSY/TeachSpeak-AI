import RootContext from "../../providers/root";
import './recording-menu.css';
import React, { useEffect, useState, useContext} from 'react';
import axios from "axios";
import ClassroomIMG from "../../pages/home-page/classroom-stock.jpg"

function RecordingMenu({setMenuSlide, setKeywordCounts}) {
    const {
        setCurrentPage
    } = useContext(RootContext);

    const [currentlyRecording, isCurrentlyRecording] = useState(false);
    const [driversList, setDriversList] = useState([]);
    const [defaultDriver, setDefaultDriver] = useState({});

    const startRecording = async () => {
        try {
            isCurrentlyRecording(true)
            const response = await axios.get("http://localhost:5000/api/start_recording");
            console.log(response.data)
        } catch (error) {
            console.error("Error starting recording:", error);
            isCurrentlyRecording(false)
        }
    }

    const stopRecording = async () => {
        try {
            const response = await axios.get("http://localhost:5000/api/stop_recording");
            console.log(response.data); // Assuming the response contains the path to the saved audio file
            isCurrentlyRecording(false)
            console.log(response)
        } catch (error) {
            console.error("Error stopping recording:", error);
            isCurrentlyRecording(true)
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

    const submit = async () => {
        setMenuSlide("loading")
        try {
            const response = await axios.get("http://localhost:5000/api/submit-audio");
            setKeywordCounts(response.data)

        } catch (error) {
            console.error("lol:", error);
        }
        setMenuSlide("results")
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
        <div class="main" style={{ backgroundImage: `url(${ClassroomIMG})` }}>
            <div className='overlay'></div>
            <div className='container'>
                <div className='center'>
                    <i className={`gg-record record-icon`} style={{ color: currentlyRecording ? '#F61B1C' : '#0094D5' }}></i> 
                    <p style={{textAlign: 'center', opacity: currentlyRecording ? '1' : '0', color: '#F61B1C', fontWeight: 'bold'}}>RECORDING</p>
                    <div className='button-container'>
                        <select onChange={(e) => setCurrentDriver(e.target.value)}>
                            <option value={defaultDriver.name}>{defaultDriver.name}</option>
                            {driversList.map((option, index) => (
                                option.name !== defaultDriver.name && (
                                    <option key={index} value={option.name}>{option.name}</option>
                                )
                            ))}
                        </select>
                        <button style={{backgroundColor: '#2FB362'}} className='start' onClick={startRecording}>Start</button>
                        <button style={{backgroundColor: '#E53430'}} className='stop' onClick={stopRecording}>Stop</button>
                        <button style={{backgroundColor: '#0094D5'}} onClick={submit}>Submit</button>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default RecordingMenu;
