import React from 'react';
import { useParams, Link } from 'react-router-dom';
import './TeamInfo.css'; // Importa los estilos de TeamInfo

const TeamInfo = ({ teams }) => {
  const { teamName } = useParams();
  const team = teams[teamName];

  if (!team) return <div>Loading...</div>;

  const positions = ["Goalkeeper", "Centre-Back", "Left-Back", "Right-Back", "Defensive Midfield", "Central Midfield", "Attacking Midfield", "Left Winger", "Right Winger", "Centre-Forward"];

  return (
    <div className="team-info">
      <img src={`http://127.0.0.1:5000/flags/${team.flag}`} alt={teamName} className="team-flag" />
      <h2>{teamName}</h2>
      <div className="players-container">
        {positions.map((position) => (
          <div key={position} className="position-group">
            <h4>{position}:</h4>
            <div className="player-list">
              {team.players.filter(player => player.position === position).map(player => (
                <div key={player.name} className="player-name">{player.name} - Goles: {player.goals}</div>
              ))}
            </div>
          </div>
        ))}
      </div>
      <div className="top-scorers">
        <h3>Máximos Goleadores:</h3>
        <div className="scorer-list">
          {team.players.sort((a, b) => b.goals - a.goals).slice(0, 5).map(player => (
            <div key={player.name} className="player-name">{player.name} - {player.goals} goles</div>
          ))}
        </div>
      </div>
      <div className="back-link">
        <Link to="/" className="back-button">Atrás</Link>
      </div>
    </div>
  );
};

export default TeamInfo;
