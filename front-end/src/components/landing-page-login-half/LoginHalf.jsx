import React, { useContext} from 'react';
import RootContext from "../../providers/root";
import './login-half.css';

function LoginHalf() {
    const {
        setCurrentPage
    } = useContext(RootContext);
    
    return (
        <div className='login-half'>
            <p className='sub-title'>Welcome to</p>
            <h1>TEACHSPEAK AI</h1>

            <form className='input-container'>
                <input type='text' placeholder='Email Address'></input>
                <input type='password' placeholder='Password'></input>
                <button onClick={() => setCurrentPage("home")}>Continue</button>
            </form>
            <p className='signup-text'>Don't have an account ? <button className='signup'>Sign up Now</button></p>

            <div className='divider-container'>
                <div />
                <p>Or</p>
                <div  />
            </div>

            <div className='social-media-login-container'>
                <p>Continue with social media</p>
                <button>Fb</button>
                <button>G</button>
                <button>L</button>
            </div>
        </div>
    );
}

export default LoginHalf;
