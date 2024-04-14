import React, { useContext} from 'react';
import RootContext from "../../providers/root";
import './results-page.css';

function ResultsPage() {
    const {
        setCurrentPage
    } = useContext(RootContext);
    
    return (
        <div className='results-page'>
            <h1>Results Page</h1>
            <button onClick={() => setCurrentPage("landing")}>Next Page</button>
        </div>
    );
}

export default ResultsPage;
