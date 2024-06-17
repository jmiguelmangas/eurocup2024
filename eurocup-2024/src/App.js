import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import axios from 'axios';
import TeamList from './components/TeamList';
import TeamInfo from './components/TeamInfo';
import './App.css'; // Importa los estilos generales de la aplicación

const App = () => {
  const [teams, setTeams] = useState({});

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/teams');
        setTeams(response.data);
      } catch (error) {
        console.error("Error fetching the teams data:", error);
      }
    };
    fetchTeams();
  }, []);

  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<TeamList teams={teams} />} />
          <Route path="/team/:teamName" element={<TeamInfo teams={teams} />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
