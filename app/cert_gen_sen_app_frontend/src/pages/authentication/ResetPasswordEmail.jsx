import React, { useState } from 'react';
import { Container, TextField, Alert, Typography, Box, Button, Grid, CircularProgress } from '@mui/material';
import { useSendPasswordResetEmailMutation } from '../../services/userAuthAPI';
import NavBar from '../../components/base_components/NavBar';

const ResetPasswordEmail = () => {

    const [error, setError] = useState({})

    const [successMsg, setSuccessMsg] = useState([])

    const [sendPasswordResetEmail, responseSendPasswordResetEmail] = useSendPasswordResetEmailMutation()

    const handlePasswordResetEmail = async (e) => {
        e.preventDefault()
        const data = new FormData(e.currentTarget)
        const actualData = {
            email: data.get('email')
        }

        const res = await sendPasswordResetEmail(actualData)

        if (res.error) {
            setSuccessMsg({});
            setError(res.error.data.errors)
        }
        if (res.data) {
            setError({})
            setSuccessMsg(res.data)
            document.getElementById('password-reset-form').reset()
        }
    }

    return (
        <>
            <NavBar />
            <Box component='form' id="password-reset-form" noValidate onSubmit={handlePasswordResetEmail}>
                <Container maxWidth="sm" sx={{ transform: "translate(0%,50%)", boxShadow: '10px 12px 20px gray', borderRadius: '5px', padding: 2 }}>
                    <Typography variant="h4" align="center" gutterBottom>Password Reset Email</Typography>
                    <TextField
                        label="Email"
                        fullWidth
                        required
                        margin="normal"
                        variant="outlined"
                        type='email'
                        id='email'
                        name='email'
                    />
                    {error.email ? <Typography>{error.email[0]}</Typography> : ""}
                    <Grid container sx={{ display: 'flex', justifyContent: 'center' }} marginTop={5} paddingBottom={1}>
                        {
                            responseSendPasswordResetEmail.isLoading ? <CircularProgress sx={{ display: 'flex', justifyContent: 'center' }} /> :
                                <Button
                                    type="submit"
                                    variant="contained"
                                    color="primary"
                                    sx={{ marginBottom: "10px", width: '100%' }}
                                >Send Email
                                </Button>
                        }
                    </Grid>
                    <Box marginTop={2}>
                        {
                            error.non_fields_errors ? <Alert severity='error'>{error.non_fields_errors}</Alert> : ""
                        }
                        {
                            successMsg.msg ? <Alert severity='success'>{successMsg.msg}</Alert> : ""
                        }
                    </Box>
                </Container>
            </Box>
        </>
    );
};

export default ResetPasswordEmail;
