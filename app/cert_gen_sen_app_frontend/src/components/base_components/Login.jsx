import React, { useState } from 'react';
import { Container, TextField, Typography, Button, Grid, Link } from '@mui/material';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import BackdropSpinner from './Backdrop';

const LoginPage = () => {

    const [openSpinner, setOpenSpinner] = useState(false)

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate()

    const handleLogin = (e) => {
        e.preventDefault();
        setOpenSpinner(true)
        setTimeout(() => { setOpenSpinner(false) }, 3000)
        const url = "http://127.0.0.1:8000/api/login/"
        axios.post(url, {
            "username": username,
            "password": password,
        }).then(res => localStorage.setItem("token", res.data.token)).then(setTimeout(() => navigate("/"), 3000)).catch(err => console.log(err))
    }

    return (
        <>
            <Container maxWidth="sm" sx={{ transform: "translate(0%,50%)" }}>
                <Typography variant="h4" align="center" gutterBottom>Login</Typography>
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
                    <Grid container justify="space-between">
                        <Button
                            type="submit"
                            variant="contained"
                            color="primary"
                            onClick={handleLogin}
                            sx={{ marginBottom: "10px" }}
                        >Login
                        </Button>
                    </Grid>
                </form>
                <Link href="/api/register" >
                    Don't have an account? Register
                </Link>
            </Container>
            <BackdropSpinner open={openSpinner} />
        </>
    );
};

export default LoginPage;
