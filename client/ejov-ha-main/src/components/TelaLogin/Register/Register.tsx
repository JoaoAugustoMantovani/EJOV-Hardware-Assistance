import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Register.css';

const Register: React.FC = () => {
  const [email, setEmail] = useState('');
  const [birthdate, setBirthdate] = useState('');
  const [gender, setGender] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  const handleRegister = () => {
    fetch('http://127.0.0.1:4000/api/user/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, birthdate, gender, password })
    })
    .then(response => response.json())
    .then(data => {
      console.log('User Registered:', data);
      navigate('/');
    })
    .catch(error => console.error('Error:', error));
  };

  const handleEmailChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setEmail(event.target.value);
  };

  const handleBirthdateChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setBirthdate(event.target.value);
  };

  const handleGenderChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setGender(event.target.value);
  };

  const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  };

  

  const calculateAge = (birthdate: string): number => {
    const today = new Date();
    const birthDate = new Date(birthdate);
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
      age--;
    }
    return age;
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const age = calculateAge(birthdate);
    if (age < 18) {
      setError('Você deve ter pelo menos 18 anos para se registrar.');
      return;
    }

   

    setError(null);
    handleRegister();
  };

  return (
    <div className="register-container">
      <div className="register-box">
        <img src="src/assets/LogoNoText.png" alt="Logo no Text" id='LogoNoText'/>
        <h2>CADASTRAR CONTA</h2>

        {error && <div className="error-message">{error}</div>}

        <form onSubmit={handleSubmit}>
          <label>E-MAIL:</label>
          <input 
            type="email" 
            placeholder="E-mail"
            value={email}
            onChange={handleEmailChange}
          />
          
          <label>DATA DE NASCIMENTO:</label>
          <input 
            type="date" 
            placeholder="Data de nascimento"
            value={birthdate}
            onChange={handleBirthdateChange}
            id='DateBox' 
            className='date-box'
          />

          <label>SEXO:</label>
          <select 
            name="Gender" 
            id="Gender"
            value={gender}
            onChange={handleGenderChange}
          >
            <option value=""></option>
            <option value="Male">Masculino</option>
            <option value="Female">Feminino</option>
            <option value="Other">Outro</option>
          </select>

          <label>SENHA:</label>
          <input 
            type="password" 
            placeholder="Senha"
            value={password}
            onChange={handlePasswordChange}
          />
          <label>CONFIRMAR SENHA:</label>
          <input 
            type="password" 
            placeholder="Confirmar senha"
            
          />
          <button type="submit">CRIAR</button>
        </form>
      </div>
    </div>
  );
};

export default Register;
