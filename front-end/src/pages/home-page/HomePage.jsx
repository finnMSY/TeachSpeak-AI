import React, { useState, useContext} from 'react';
import RootContext from "../../providers/root";
import './home-page.css';
import { RecordingMenu, Progress, History, Settings, Loading, Results } from '../../components';

function HomePage() {
    const {
        setCurrentPage
    } = useContext(RootContext);

    const [menuSlide, setMenuSlide] = useState('');
    const [keywordCounts, setKeywordCounts] = useState({});

    const renderComponent = () => {
        switch (menuSlide) {
            case 'progress':
                return <Progress />;
            case 'history':
                return <History />;
            case 'settings':
                return <Settings />;
            case 'loading':
                return <Loading />
            case 'results':
                return <Results keywordCounts={keywordCounts}/>
            default:
                return <RecordingMenu setMenuSlide={setMenuSlide} setKeywordCounts={setKeywordCounts} />;
        }
    };

    return (
        <div className='home'>
            {renderComponent()}
            <div class="header">
                <ul>
                    <li className='title'><button onClick={() => setCurrentPage("")}>TeachSpeakAI</button></li>
                    <li><button><i class="gg-profile"></i></button></li>
                    <li><button><i class="gg-bell"></i></button></li>
                </ul>                
                </div>
                <div class="navigation">
                <ul>
                    <li><button onClick={() => setMenuSlide('')} className={menuSlide === '' || menuSlide === 'loading' || menuSlide === 'results' ? 'active' : ''}><i class="gg-record"></i>Record Session</button></li>
                    <li><button onClick={() => setMenuSlide('progress')} className={menuSlide === 'progress' ? 'active' : ''}><i class="gg-arrow-right-o"></i> Progress</button></li>
                    <li><button onClick={() => setMenuSlide('history')} className={menuSlide === 'history' ? 'active' : ''}><i class="gg-time"></i> History</button></li>
                    <li><button onClick={() => setMenuSlide('settings')} className={menuSlide === 'settings' ? 'active' : ''}><i class="gg-shape-hexagon"></i>Settings</button></li>
                </ul>
            </div>
        </div>
    );
}

export default HomePage;
