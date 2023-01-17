import React from "react";
import Home from "./Home";
import { AllEvents } from "./components/event_components/AllEvents";
import SpecificEvent from "./components/event_components/SpecificEvent";
import LoginPage from "./components/base_components/Login";
import RegisterPage from "./components/base_components/Register";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import PrivateRoutes from "./PrivateRoutes";

function App() {
  return (
    <Router>
      <Routes>
        <Route element={<PrivateRoutes />}>
          <Route path="/" element={<Home />} />
          <Route path="/api/all-events" element={<AllEvents />} />
          <Route path="/api/event/:slug" element={<SpecificEvent />} />
          <Route path="/api/create-event/" element={<Home />} />
          <Route path="/api/issue-certificate/" element={<Home />} />
        </Route>
        <Route path="/api/login" element={<LoginPage />} />
        <Route path="/api/register" element={<RegisterPage />} />
      </Routes>
    </Router>
  );
}

export default App;
