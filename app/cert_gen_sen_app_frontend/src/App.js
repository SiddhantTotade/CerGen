import React from "react";
import Home from "./Home";
import { AllEvents } from "./components/event_components/AllEvents";
import SpecificEvent from "./components/event_components/SpecificEvent";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/api/all-events" element={<AllEvents />} />
        <Route path="/api/all-events/:slug" element={<SpecificEvent />} />
        <Route path="/api/create-event/" element={<Home />} />
        <Route path="/api/issue-certificate/" element={<Home />} />
      </Routes>
    </Router>
  );
}

export default App;
