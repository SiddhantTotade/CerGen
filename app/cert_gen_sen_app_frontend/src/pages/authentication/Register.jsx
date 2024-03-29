import React, { useState } from 'react';
import { Container, TextField, Typography, Checkbox, Button, Grid, FormControlLabel, CircularProgress, Alert } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import { storeToken } from '../../services/LocalStorageService';
import { useRegisterUserMutation } from '../../services/userAuthAPI';
import { Box } from '@mui/system';

const RegisterPage = () => {

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
            password2: data.get('password2'),
            tc: data.get('tc')
        }

        const res = await registerUser(actualData)

        if (res.error) {
            setError(res.error.data.errors)
        }
        if (res.data) {
            storeToken(res.data.token)
            navigate('/home')
        }
    }

    return (
        <Box noValidate id='registration-form' onSubmit={handleRegister} component='form' >
            <Container maxWidth="sm" sx={{ transform: "translate(0%,35%)", boxShadow: '10px 12px 20px gray', borderRadius: '5px', padding: 2 }}>
                <Typography variant="h4" align="center" gutterBottom >Register</Typography>
                <TextField
                    label="Name"
                    fullWidth
                    margin="normal"
                    variant="outlined"
                    type='name'
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
                <FormControlLabel sx={{ marginTop: '13px' }} label="I agree to terms and conditions" control={<Checkbox value={true} color='primary' name='tc' id='tc' />}></FormControlLabel>
                <Grid container justify="space-between" marginTop={5} >
                    {
                        isLoading ? <CircularProgress /> :
                            <Button
                                type="submit"
                                variant="contained"
                                color="primary"
                                sx={{ marginBottom: "10px", width: '100%' }}
                            >
                                Register
                            </Button>
                    }
                </Grid>
                <Box marginTop={1}>
                    {
                        error.non_field_errors ? <Alert severity='error'>{error.non_field_errors[0]}</Alert> : ""
                    }
                </Box>
            </Container>
        </Box>
    );
};

export default RegisterPage;
