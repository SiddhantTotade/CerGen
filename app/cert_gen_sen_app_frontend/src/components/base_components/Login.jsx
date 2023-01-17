import React, { useState } from 'react';
import { Container, TextField, Typography, Button, Grid, Link } from '@mui/material';

const LoginPage = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [isRegister, setIsRegister] = useState(false);

    const handleLogin = (e) => {
        e.preventDefault();
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
                    <Link href="#" onClick={() => setIsRegister(!isRegister)}>
                        {isRegister ? 'Already have an account? Login' : 'Don\'t have an account? Register'}
                    </Link>
                </Grid>
            </form>
        </Container>
    );
};

export default LoginPage;
