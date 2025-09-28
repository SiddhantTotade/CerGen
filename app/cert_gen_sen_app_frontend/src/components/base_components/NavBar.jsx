import React from 'react'
import { AppBar, Box, Toolbar, Typography, Button } from '@mui/material'
import { NavLink } from 'react-router-dom'

const NavBar = () => {

    return (
        <Box sx={{ flexGrow: 1 }}>
            <AppBar position='static' color='primary' >
                <Toolbar>
                    <Typography variant='h5' component='div' sx={{ flexGrow: 1, fontFamily: 'Bruno Ace' }} >CerGen</Typography>
                    <Button style={({ isActive }) => { return { backgroundColor: isActive ? "#026ab7" : "" } }} component={NavLink} to='/api/login' sx={{ color: "white", textTransform: "None" }} >Sign In</Button>
                    <Button style={({ isActive }) => { return { backgroundColor: isActive ? "#026ab7" : "" } }} component={NavLink} to='/api/register' sx={{ color: "white", textTransform: "None" }} >Sign Up</Button>
                </Toolbar>
            </AppBar>
        </Box>
    )
}

export default NavBar