import React, { useState, useContext} from 'react';
import RootContext from "../../providers/root";
import './home-page.css';
import ClassroomIMG from "./classroom-stock.jpg"
import { RecordingMenu, Progress, History, Settings } from '../../components';

function HomePage() {
    const {
        setCurrentPage
    } = useContext(RootContext);

    const [menuSlide, setMenuSlide] = useState();

    const renderComponent = () => {
        switch (menuSlide) {
            case 'progress':
                return <Progress />;
            case 'history':
                return <History />;
            case 'settings':
                return <Settings />;
            default:
                return <RecordingMenu />;
        }
    };

    return (
        <div className='home'>
            <div class="main" style={{ backgroundImage: `url(${ClassroomIMG})` }}>
                <div className='overlay'></div>
                {renderComponent()}
            </div>
            <div class="header">
                <ul>
                    <li className='title'><button onClick={() => setCurrentPage("")}>TeachSpeakAI</button></li>
                    <li><button><i class="gg-profile"></i></button></li>
                    <li><button><i class="gg-bell"></i></button></li>
                </ul>                
                </div>
                <div class="navigation">
                <ul>
                    <li><button onClick={() => setMenuSlide('')} className={menuSlide === '' ? 'active' : ''}><i class="gg-record"></i>Record Session</button></li>
                    <li><button onClick={() => setMenuSlide('progress')} className={menuSlide === 'progress' ? 'active' : ''}><i class="gg-arrow-right-o"></i> Progress</button></li>
                    <li><button onClick={() => setMenuSlide('history')} className={menuSlide === 'history' ? 'active' : ''}><i class="gg-time"></i> History</button></li>
                    <li><button onClick={() => setMenuSlide('settings')} className={menuSlide === 'settings' ? 'active' : ''}><i class="gg-shape-hexagon"></i>Settings</button></li>
                </ul>
            </div>
        </div>
    );
}

export default HomePage;
