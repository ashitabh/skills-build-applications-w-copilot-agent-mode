import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

// Replace the hardcoded URL with a dynamic environment variable or a placeholder for easier configuration
const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch(`${API_BASE_URL}/api/users`)
      .then(response => response.json())
      .then(data => setUsers(data));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Users</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user.id}>
              <td>{user.id}</td>
              <td>{user.name}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Users;
