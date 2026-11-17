import React, {useState } from 'react';
import './login.css';
import { useNavigate } from 'react-router';

interface LoginProps{
    onLoginSuccess?: (email:string) => void;
}

const Login: React.FC<LoginProps> = ({ onLoginSuccess}) => {
    const navigate = useNavigate()

    const [email, setEmail] = useState<string>('');
    const [password, setPassword] = useState<string>('');
    const [error, setError] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState<boolean> (false);

const handleSubmit = async (e: React.SubmitEvent<HTMLFormElement>) => {
    e.preventDefault()
    setError(null)

    if(!email.trim() || !password.trim()){
        setError('Please enter both your email and password');
        return;
    }

    setIsLoading(true)
    try{
        console.log('Submitting login:', {email, password});

        await new Promise((resolve) => setTimeout(resolve, 800));

        if(onLoginSuccess){
            onLoginSuccess(email);
        }
    }
    catch(err){
        setError('Invalid email or password. Please try again.');
    }
    finally{
        navigate('/welcome', { replace: true });
        setIsLoading(false)
    }
    }

return (
    <div className="login-container">
    <form className='login-form' onSubmit={handleSubmit} noValidate>
        <h2>Sign In</h2>

        {error && (
            <div className= "error-message" role="alert">
                {error}
            </div>
        )}

        <div className="form-group">
            <label htmlFor="email">Email Address</label>
          <input
            id="email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="you@example.com"
            required
            disabled={isLoading}
          />
        </div>

        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            id="password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="••••••••"
            required
            disabled={isLoading}
          />
        </div>
        <button type="submit" className="login-button" disabled={isLoading}>
            {isLoading ? 'Signing in...' : 'Log In'}
        </button>
    </form>
    </div>  
);
};

export default Login;

