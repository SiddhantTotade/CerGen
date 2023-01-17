import { Outlet, Navigate } from "react-router-dom";

export default function PrivateRoutes() {

    console.log(localStorage.getItem('token'));

    let auth = { 'token': false }

    if (localStorage.getItem("token")) {
        auth = { 'token': true }
    }

    return (
        auth.token ? <Outlet /> : <Navigate to="/api/login" />
    )
} 