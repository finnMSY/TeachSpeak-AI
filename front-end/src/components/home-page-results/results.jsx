import RootContext from "../../providers/root";
import './results.css';
import React, { useContext} from 'react';

function Results({keywordCounts}) {
    const {
        setCurrentPage
    } = useContext(RootContext);
    
    return (
        <div>
           {Object.entries(keywordCounts).map(([keyword, count]) => (
                <div key={keyword}>
                    {keyword}: {count}
                </div>
            ))}
        </div>
    );
}

export default Results;
