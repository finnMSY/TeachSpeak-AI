import RootContext from "../../providers/root";
import './progress.css';
import React, { useContext} from 'react';

function Progress() {
    const {
        setCurrentPage
    } = useContext(RootContext);
    
    return (
        <div className='container'>
            <div className='center'>
                <h1>Progress</h1>
            </div>
        </div>
    );
}

export default Progress;
