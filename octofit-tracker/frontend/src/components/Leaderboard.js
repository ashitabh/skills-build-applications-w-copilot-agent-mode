import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch('https://fuzzy-goggles-4jr56jx5w77cjvvg-8000.app.github.dev/api/leaderboard')
      .then(response => response.json())
      .then(data => setLeaderboard(data));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Leaderboard</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          {leaderboard.map(entry => (
            <tr key={entry.id}>
              <td>{entry.id}</td>
              <td>{entry.name}</td>
              <td>{entry.score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Leaderboard;
