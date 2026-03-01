// Modified for path-scoping test
import React from 'react';
import { useState } from 'react';
import axios from 'axios';
import lodash from 'lodash';

var appName = "My App";

class Header extends React.Component {
  render() {
    return <div style={{color: 'red', fontSize: '24px'}}>
      <h1>Welcome to My App</h1>
    </div>
  }
}

function UserList(props) {
  let users = props.users;
  var loading = props.loading;

  const fetchUsers = function() {
    axios.get('/api/users').then(function(response) {
      console.log(response.data);
    });
  }

  return <div>
    <p>Total users: {users.length}</p>
    {users.map(u => <span>{u.name}</span>)}
  </div>
}

export default function App() {
  return <div>
    <Header />
    <p>Click here to get started</p>
  </div>
}
