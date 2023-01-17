import React, { useState, useEffect } from 'react';
import { Container, TextField, Typography, Button, Grid, Link } from '@mui/material';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const LoginPage = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [isRegister, setIsRegister] = useState(false);
    const navigate = useNavigate()

    const [authenticated, setauthenticated] = useState(null);

    // useEffect(() => {
    //     const loggedInUser = localStorage.getItem("token");
    //     if (loggedInUser) {
    //         setauthenticated(loggedInUser);
    //     }
    // },[]);

    // if (authenticated) {
    //     navigate("/")
    // }
    // else {
    //     navigate("/api/login")
    // }

    const handleLogin = (e) => {
        e.preventDefault();
        const url = "http://127.0.0.1:8000/api/login/"
        axios.post(url, {
            "username": username,
            "password": password,
        }).then(res => localStorage.setItem("token", res.data.token)).then(localStorage.getItem("token") === "" ? navigate("/api/login") : navigate("/")).catch(err => console.log(err))
        // Perform login logic here
    }

    const handleRegister = (e) => {
        e.preventDefault();
        // Perform registration logic here
    }

    return (
        <Container maxWidth="sm">
            <Typography variant="h4" align="center" gutterBottom>
                {isRegister ? 'Register' : 'Login'}
            </Typography>
            <form>
                <TextField
                    label="Username"
                    fullWidth
                    margin="normal"
                    variant="outlined"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <TextField
                    label="Password"
                    fullWidth
                    margin="normal"
                    variant="outlined"
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                {isRegister && (
                    <TextField
                        label="Confirm Password"
                        fullWidth
                        margin="normal"
                        variant="outlined"
                        type="password"
                    // Additional registration fields can be added here
                    />
                )}
                <Grid container justify="space-between">
                    <Button
                        type="submit"
                        variant="contained"
                        color="primary"
                        onClick={isRegister ? handleRegister : handleLogin}
                    >
                        {isRegister ? 'Register' : 'Login'}
                    </Button>
                </Grid>
            </form>
            <Link href="#" className='' onClick={() => setIsRegister(!isRegister)}>
                {isRegister ? 'Already have an account? Login' : 'Don\'t have an account? Register'}
            </Link>
        </Container>
    );
};

export default LoginPage;
