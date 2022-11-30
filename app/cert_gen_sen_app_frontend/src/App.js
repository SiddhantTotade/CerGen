import React from "react";
import Home from "./Home";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/api/all-events" element={<Home />} />
        <Route path="/api/create-event/" element={<Home />} />
        <Route path="/api/issue-certificate/" element={<Home />} />
      </Routes>
    </Router>
  );
}

export default App;
