import React, { useContext} from 'react';
import RootContext from "../../providers/root";
import './title-half.css';
import ClassroomIMG from "./classroom-stock.jpg"

function TitleHalf() {
    const {
        setCurrentPage
    } = useContext(RootContext);
    
    return (
        <div className='title-half'>
            <h1 className='center'>TEACHSPEAK AI</h1>
            <p className='center'>An do on frankness so cordially immediate recommend contained. Imprudence insensible be literature unsatiable do. </p>

            <div className='overlay'></div>
            <img src={ClassroomIMG} />
        </div>
    );
}

export default TitleHalf;
