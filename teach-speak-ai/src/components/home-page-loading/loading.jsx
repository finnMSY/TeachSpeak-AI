import RootContext from "../../providers/root";
import './loading.css';
import React, { useContext} from 'react';
import ClassroomIMG from "../../pages/home-page/classroom-stock.jpg"

function Loading() {
    const {
        setCurrentPage
    } = useContext(RootContext);
    
    return (
        <div class="main" style={{ backgroundImage: `url(${ClassroomIMG})` }}>
            <div className='overlay'></div>
            <div className='container'>
            <div className="loader-container"><div class="loader"></div></div>
            </div>
        </div>
    );
}

export default Loading;
