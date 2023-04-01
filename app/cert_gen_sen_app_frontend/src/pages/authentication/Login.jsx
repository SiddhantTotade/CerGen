import React, { useState, useEffect } from 'react';
import { Container, TextField, Typography, Button, Grid, Link, CircularProgress } from '@mui/material';
import { useNavigate } from 'react-router-dom'
import { useLoginUserMutation } from '../../services/userAuthAPI';
import { getToken, storeToken } from '../../services/LocalStorageService';
import { useDispatch } from 'react-redux';
import { setUserToken } from '../../features/authSlice';

const LoginPage = () => {

    const [error, setError] = useState({})

    const dispatch = useDispatch()

    const navigate = useNavigate()

    const [loginUser, { isLoading }] = useLoginUserMutation()

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
            navigate('/')
        }
    }

    let { access_token } = getToken()

    useEffect(() => {
        dispatch(setUserToken({ access_token: access_token }))
    }, [access_token, dispatch])

    return (
        <>
            <Container maxWidth="sm" sx={{ transform: "translate(0%,50%)" }}>
                <Typography variant="h4" align="center" gutterBottom>Login</Typography>
                <form>
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
                                    onClick={handleLogin}
                                    sx={{ marginBottom: "10px" }}
                                >Login
                                </Button>
                        }
                    </Grid>
                </form>
                <Link href="/api/register" >
                    Don't have an account? Register
                </Link>
            </Container>
        </>
    );
};

export default LoginPage;
