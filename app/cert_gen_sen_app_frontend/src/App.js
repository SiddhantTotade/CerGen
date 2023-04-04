import React from "react";
import Home from "./Home";
import { AllEvents } from "./pages/AllEvents";
import SpecificEvent from "./pages/SpecificEvent";
import LoginPage from "./pages/authentication/Login";
import RegisterPage from "./pages/authentication/Register";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
// import PrivateRoutes from "./PrivateRoutes";
import { Navigate } from "react-router-dom";
import { useSelector } from "react-redux";
import Layout from "./pages/Layout";

function App() {
  const { access_token } = useSelector((state) => state.auth);

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route path="/api/login" element={<LoginPage />} />
          <Route path="/api/register" element={<RegisterPage />} />
          {/* <Route
            index
            element={!access_token ? <LoginPage /> : <Navigate to="/home" />}
          /> */}
        </Route>

        <Route
          path="/api/home"
          element={access_token ? <Home /> : <Navigate to="/api/login" />}
        />

        <Route path="/api/all-events" element={<AllEvents />} />
        <Route path="/api/event/:slug" element={<SpecificEvent />} />

        <Route path="*" element={<h1>Error 404. Page not found.</h1>} />

        {/* <Route element={<PrivateRoutes />}>
          <Route path="/" element={<Home />} />
          <Route path="/api/all-events" element={<AllEvents />} />
          <Route path="/api/event/:slug" element={<SpecificEvent />} />
          <Route path="/api/create-event/" element={<Home />} />
          <Route path="/api/issue-certificate/" element={<Home />} />
        </Route>
        <Route path="/api/login" element={<LoginPage />} />
        <Route path="/api/register" element={<RegisterPage />} /> */}
      </Routes>
    </Router>
  );
}

export default App;
