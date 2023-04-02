import React, { useState } from 'react';
import { Container, TextField, Typography, Button, Grid, Link, FormControlLabel, CircularProgress } from '@mui/material';
// import axios from 'axios';
import { NavLink, useNavigate } from 'react-router-dom';
import { storeToken } from '../../services/LocalStorageService';
import { useRegisterUserMutation } from '../../services/userAuthAPI';
import { Box } from '@mui/system';
import { CheckBox } from '@mui/icons-material';

const RegisterPage = () => {
    // const [username, setUsername] = useState('');
    // const [password, setPassword] = useState('');
    // const [email, setEmail] = useState('');
    // const [isRegister, setIsRegister] = useState(false);
    // const navigate = useNavigate()

    // const handleRegister = (e) => {
    //     e.preventDefault();
    //     const url = "http://127.0.0.1:8000/api/register/"
    //     axios.post(url, {
    //         "username": username,
    //         "email": email,
    //         "password": password,
    //     }).then(res => localStorage.setItem("token", res.data.token)).then(setTimeout(() => navigate("/"), 3000)).catch(err => console.log(err))
    // }

    const [error, setError] = useState({})

    const navigate = useNavigate()

    const [registerUser, { isLoading }] = useRegisterUserMutation()

    const handleRegister = async (e) => {
        e.preventDefault()
        const data = new FormData(e.currentTarget)
        const actualData = {
            name: data.get('name'),
            email: data.get('email'),
            password: data.get('password'),
            passwoord2: data.get('password2'),
            tc: data.get('tc')
        }

        const res = await registerUser(actualData)

        if (res.error) {
            setError(res.data.token)
        }
        if (res.data) {
            storeToken(res.data.token)
            navigate('/home')
        }
    }

    return (
        <Box noValidate id='registration-form' onSubmit={handleRegister} component='form'>
            <Container maxWidth="sm" sx={{ transform: "translate(0%,50%)" }}>
                <Typography variant="h4" align="center" gutterBottom>Register</Typography>
                <TextField
                    label="Name"
                    fullWidth
                    margin="normal"
                    variant="outlined"
                    name='name'
                    id='name'
                />
                {error.name ? <Typography>{error.name[0]}</Typography> : ""}
                <TextField
                    label="Email"
                    fullWidth
                    margin="normal"
                    variant="outlined"
                    type="email"
                    name='email'
                    id='email'
                />
                {error.email ? <Typography>{error.email[0]}</Typography> : ""}
                <TextField
                    label="Password"
                    fullWidth
                    margin="normal"
                    variant="outlined"
                    type="password"
                    name='password'
                    id='password'
                />
                {error.password ? <Typography>{error.password[0]}</Typography> : ""}
                <TextField
                    label="Confirm Password"
                    fullWidth
                    margin="normal"
                    variant="outlined"
                    type="password"
                    name='password2'
                    id='password2'
                />
                {error.password ? <Typography>{error.password[0]}</Typography> : ""}
                <FormControlLabel label="I agree to terms and conditions" control={<CheckBox value={true} name='tc' id='tc' />}></FormControlLabel>
                <Grid container justify="space-between">
                    {
                        isLoading ? <CircularProgress /> :
                            <Button
                                type="submit"
                                variant="contained"
                                color="primary"
                                sx={{ marginBottom: "10px" }}
                            >
                                Register
                            </Button>
                    }
                </Grid>
                <Link href="/api/login">
                    Already have an account? Login
                </Link>
            </Container>
        </Box>
    );
};

export default RegisterPage;
