import RootContext from "../../providers/root";
import './history.css';
import React, { useContext} from 'react';

function History() {
    const {
        setCurrentPage
    } = useContext(RootContext);
    
    return (
        <div className='container'>
            <div className='center'>
                <h1>History</h1>
            </div>
        </div>
    );
}

export default History;
