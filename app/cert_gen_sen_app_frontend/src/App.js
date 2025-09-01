import React from "react";
import Home from "./Home";
import { AllEvents } from "./pages/AllEvents";
import SpecificEvent from "./pages/SpecificEvent";
import LoginPage from "./pages/authentication/Login";
import RegisterPage from "./pages/authentication/Register";
import ResetPasswordEmail from "./pages/authentication/ResetPasswordEmail";
import ResetPassword from "./pages/authentication/ResetPassword";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { Navigate } from "react-router-dom";
import { useSelector } from "react-redux";
import Layout from "./pages/Layout";

function App() {
  const { access_token } = useSelector((state) => state.auth);

  return (
    <Router>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/api/login" element={<LoginPage />} />
          <Route index path="/api/home" element={<Home />} />
          <Route path="/api/register" element={<RegisterPage />} />
          <Route
            index
            element={
              !access_token ? (
                <Navigate to="/api/login" />
              ) : (
                <Navigate to="/api/home" />
              )
            }
          />
        </Route>

        <Route
          path="/api/home"
          element={
            access_token ? (
              <Navigate to="/api/home" />
            ) : (
              <Navigate to="/api/login" />
            )
          }
        />

        <Route path="/api/all-events" element={<AllEvents />} />
        <Route path="/api/event/:slug" element={<SpecificEvent />} />
        <Route path="/reset-password-email" element={<ResetPasswordEmail />} />
        <Route
          path="/api/user/reset-password/:id/:token"
          element={<ResetPassword />}
        />

        <Route path="*" element={<h1>Error 404. Page not found.</h1>} />
      </Routes>
    </Router>
  );
}

export default App;
