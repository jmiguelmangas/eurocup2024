import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import './TeamList.css';

const groups = {
  "Group A": ["Germany", "Scotland", "Switzerland", "Hungary"],
  "Group B": ["Spain", "Croatia", "Albania", "Italy"],
  "Group C": ["Slovenia", "Denmark", "Serbia", "England"],
  "Group D": ["Poland", "Netherlands", "Austria", "France"],
  "Group E": ["Belgium", "Slovakia", "Romania", "Ukraine"],
  "Group F": ["Turkey", "Georgia", "Portugal", "CzechRepublic"]
};

const TeamList = ({ teams }) => {
  const [standings, setStandings] = useState({});
  const [matches, setMatches] = useState({});

  useEffect(() => {
    const fetchStandings = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/standings');
        setStandings(response.data);
      } catch (error) {
        console.error("Error fetching the standings data:", error);
      }
    };
    const fetchMatches = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/matches');
        setMatches(response.data);
      } catch (error) {
        console.error("Error fetching the matches data:", error);
      }
    };
    fetchStandings();
    fetchMatches();
  }, []);

  const handleScoreChange = async (group, index, team, newScore) => {
    const updatedMatches = { ...matches };
    updatedMatches[group][index].score = team === 'team1'
      ? `${newScore}-${updatedMatches[group][index].score.split('-')[1]}`
      : `${updatedMatches[group][index].score.split('-')[0]}-${newScore}`;

    setMatches(updatedMatches);

    try {
      await axios.post('http://127.0.0.1:5000/matches', {
        group,
        match_index: index,
        score: updatedMatches[group][index].score
      });

      // Fetch the updated standings
      const response = await axios.get('http://127.0.0.1:5000/standings');
      setStandings(response.data);

    } catch (error) {
      console.error("Error saving score:", error);
    }
  };

  return (
    <div className="team-list">
      <div className="title">
        <img src="/assets/euro2024-logo.png" alt="UEFA Euro 2024" className="logo" />
        <h1>UEFA EURO 2024 Teams</h1>
      </div>
      <div className="groups-container">
        {Object.keys(groups).map(groupName => (
          <div key={groupName} className="group">
            <h2>{groupName}</h2>
            <div className="flags-container">
              {groups[groupName].map(teamName => (
                <Link to={`/team/${teamName}`} key={teamName} className="flag-link">
                  <img src={`http://127.0.0.1:5000/flags/${teams[teamName]?.flag}`} alt={teamName} className="flag" />
                  <div className="flag-name">{teamName}</div>
                </Link>
              ))}
            </div>
            <div className="standings-container">
              <table className="standings-table">
                <thead>
                  <tr>
                    <th>Team</th>
                    <th>Played</th>
                    <th>Scored</th>
                    <th>Conceded</th>
                    <th>Goal Difference</th>
                    <th>Points</th>
                  </tr>
                </thead>
                <tbody>
                  {standings[groupName]?.map((team, index) => (
                    <tr key={team.team} className={`standing-row position-${index + 1}`}>
                      <td className="team-cell">
                        <img src={`http://127.0.0.1:5000/flags/${team.flag}`} alt={team.team} className="flag-small" />
                        <span>{team.team}</span>
                      </td>
                      <td>{team.played}</td>
                      <td>{team.scored}</td>
                      <td>{team.conceded}</td>
                      <td>{team.goal_difference}</td>
                      <td><strong>{team.points}</strong></td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <div className="matches-container">
              <h3>Matches</h3>
              {matches[groupName]?.map((match, index) => (
                <div key={index} className="match">
                  <span>{match.team1} vs {match.team2}</span>
                  <div className="score-inputs">
                    <input
                      type="number"
                      value={match.score ? match.score.split('-')[0] : ''}
                      onChange={(e) => handleScoreChange(groupName, index, 'team1', e.target.value)}
                      min="0"
                    />
                    <span> - </span>
                    <input
                      type="number"
                      value={match.score ? match.score.split('-')[1] : ''}
                      onChange={(e) => handleScoreChange(groupName, index, 'team2', e.target.value)}
                      min="0"
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TeamList;
