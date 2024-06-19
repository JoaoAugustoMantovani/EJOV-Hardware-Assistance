import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Login.css';

const Login: React.FC = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    console.log('Tentando fazer login com:', { username, password }); // Adicionando log para depuração
    fetch('http://127.0.0.1:4000/api/user/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username, password })
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Erro na solicitação de login');
      }
      return response.json();
    })
    .then(data => {
      if (data.message === 'Login successful') {
        console.log('Login bem-sucedido:', data.user);
      } else {
        console.error('Erro de login:', data.message);
      }
    })
    .catch(error => console.error('Error:', error));
  };

  const handleUsernameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    handleLogin();
  };

  return (
    <div className="login-container">
      <div className="login-box">
        <div className="logo">
          <img src="src/assets/Logo.png" alt='EJOV Logo'></img>
        </div>

        <form onSubmit={handleSubmit}>
          <label>E-MAIL:</label>
          <input 
            type="text" 
            placeholder="Login"
            value={username}
            onChange={handleUsernameChange}
          />
          
          <label>SENHA:</label>
          <input 
            type="password" 
            placeholder="Senha"
            value={password}
            onChange={handlePasswordChange}
          />

          <Link to="/reset-password" className="forgot-password">
            Esqueceu a senha?
          </Link>
          
          <button type="submit">ENTRAR</button>
        </form>

        <div className="register-link">
          Não possui uma conta? <Link to="/register">Cadastrar conta</Link>
        </div>
      </div>
    </div>
  );
};

export default Login;
