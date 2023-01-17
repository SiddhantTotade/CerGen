import React, { useState } from 'react';
import { Container, TextField, Typography, Button, Grid, Link } from '@mui/material';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const RegisterPage = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [isRegister, setIsRegister] = useState(false);
    const navigate = useNavigate()

    const handleRegister = (e) => {
        e.preventDefault();
        const url = "http://127.0.0.1:8000/api/register/"
        axios.post(url, {
            "username": username,
            "email": email,
            "password": password,
        }).then(res => localStorage.setItem("token", res.data.token)).then(setTimeout(() => navigate("/"), 3000)).catch(err => console.log(err))
    }

    return (
        <>
            <Container maxWidth="sm" sx={{ transform: "translate(0%,50%)" }}>
                <Typography variant="h4" align="center" gutterBottom>Register</Typography>
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
                        label="Email"
                        fullWidth
                        margin="normal"
                        variant="outlined"
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
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
                    <Grid container justify="space-between">
                        <Button
                            type="submit"
                            variant="contained"
                            color="primary"
                            onClick={handleRegister}
                            sx={{ marginBottom: "10px" }}
                        >
                            Register
                        </Button>
                    </Grid>
                </form>
                <Link href="/api/login" className='' onClick={() => setIsRegister(!isRegister)}>
                    Already have an account? Login
                </Link>
            </Container>
        </>
    );
};

export default RegisterPage;
