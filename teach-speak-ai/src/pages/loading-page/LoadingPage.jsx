import React, { useContext} from 'react';
import RootContext from "../../providers/root";
import './loading-page.css';

function LoadingPage() {
    const {
        setCurrentPage
    } = useContext(RootContext);
    
    return (
        <div className='loading-page'>
            <h1>Loading Page</h1>
            <button onClick={() => setCurrentPage("results")}>Next Page</button>
        </div>
    );
}

export default LoadingPage;
