import React from "react";
import Home from "./Home";
import { AllEvents } from "./pages/AllEvents";
import SpecificEvent from "./pages/SpecificEvent";
import LoginPage from "./pages/authentication/Login";
import RegisterPage from "./pages/authentication/Register";
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
