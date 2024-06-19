import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/TelaLogin/Login/Login';
import Register from './components/TelaLogin/Register/Register';

const App: React.FC = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:4000/api/data')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </Router>
  );
};

export default App;
