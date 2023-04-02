import React, { useState, useEffect } from 'react';
import { Container, TextField, Typography, Box, Button, Grid, Link, CircularProgress } from '@mui/material';
import { NavLink, useNavigate } from 'react-router-dom'
import { useLoginUserMutation } from '../../services/userAuthAPI';
import { getToken, storeToken } from '../../services/LocalStorageService';
import { useDispatch } from 'react-redux';
import { setUserToken } from '../../features/authSlice';

const LoginPage = () => {

    const [error, setError] = useState({})

    const navigate = useNavigate()

    const dispatch = useDispatch()

    const [loginUser, { isLoading }] = useLoginUserMutation()

    let { access_token } = getToken()

    const handleLogin = async (e) => {
        e.preventDefault()
        const data = new FormData(e.currentTarget)
        const actualData = {
            email: data.get('email'),
            password: data.get('password')
        }

        const res = await loginUser(actualData)

        if (res.error) {
            setError(res.error.data.errors)
        }
        if (res.data) {
            storeToken(res.data.token)
            let { access_token } = getToken()
            dispatch(setUserToken({ access_token: access_token }))
            navigate('/home')
        }
    }

    useEffect(() => {
        dispatch(setUserToken({ access_token: access_token }))
    }, [access_token, dispatch])

    return (
        <Box component='form' id='login-form' noValidate onSubmit={handleLogin}>
            <Container maxWidth="sm" sx={{ transform: "translate(0%,50%)" }}>
                <Typography variant="h4" align="center" gutterBottom>Login</Typography>
                <TextField
                    label="Username"
                    fullWidth
                    required
                    margin="normal"
                    variant="outlined"
                />
                {error.email ? <Typography>{error.email[0]}</Typography> : ""}
                <TextField
                    label="Password"
                    fullWidth
                    required
                    margin="normal"
                    variant="outlined"
                    type="password"
                />
                {error.password ? <Typography>{error.password[0]}</Typography> : ""}
                <Grid container justify="space-between">
                    {
                        isLoading ? <CircularProgress /> :
                            <Button
                                type="submit"
                                variant="contained"
                                color="primary"
                                sx={{ marginBottom: "10px" }}
                            >Login
                            </Button>
                    }
                </Grid>
                <NavLink to='/reset-password-email' >Forgot Password</NavLink>
                <Typography> Don't have an account?
                    <Link href="/api/register" >
                        Register
                    </Link>
                </Typography >
            </Container>
        </Box>
    );
};

export default LoginPage;
