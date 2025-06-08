import RootContext from "../../providers/root";
import './settings.css';
import React, { useContext} from 'react';

function Settings() {
    const {
        setCurrentPage
    } = useContext(RootContext);

    return (
        <div className='container'>
            <div className='center'>
                <h1>Settings</h1>
            </div>
        </div>
    );
}

export default Settings;
