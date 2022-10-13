import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';


function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/api/profesores/1234').then(res => res.json()).then(data => {
      setCurrentTime(data.nombre);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        ... no changes in this part ...

        <p>The current professor is {currentTime}.</p>
      </header>
    </div>
  );
}

export default App;
