import React, { useContext} from 'react';
import { TitleHalf, LoginHalf } from "../../components"
import RootContext from "../../providers/root";
import './landing-page.css';

function LandingPage() {
    const {
        setCurrentPage
    } = useContext(RootContext);
    
    return (
        <div className='landing-page'>
            <div className='landing-page-login'>
                <LoginHalf />
            </div>
            <div className='landing-page-title'>
                <TitleHalf />
            </div>
        </div>
    );
}

export default LandingPage;
