import React from 'react'
import { AppBar, Box, Toolbar, Typography, Button } from '@mui/material'
import { NavLink } from 'react-router-dom'
import { getToken } from '../../services/LocalStorageService'

const NavBar = () => {
    const { access_token } = getToken()
    return (
        <Box sx={{ flexGrow: 1 }}>
            <AppBar position='static' color='secondary' >
                <Toolbar>
                    <Typography variant='h5' component='div' sx={{ flexGrow: 1 }} >CerGen</Typography>
                    <Button style={({ isActive }) => { return { backgroundColor: isActive ? "#6d1b7b" : "" } }} component={NavLink} to='/api/login' sx={{ color: "white", textTransform: "None" }} >Sign In</Button>
                    <Button style={({ isActive }) => { return { backgroundColor: isActive ? "#6d1b7b" : "" } }} component={NavLink} to='/api/register' sx={{ color: "white", textTransform: "None" }} >Sign Up</Button>
                    {/* {
                        access_token ? <Button style={({ isActive }) => { return { backgroundColor: isActive ? "#6d1b7b" : "" } }} component={NavLink} to='/home' sx={{ color: "white", textTransform: "None" }} >Home</Button> : <Button style={({ isActive }) => { return { backgroundColor: isActive ? "#6d1b7b" : "" } }} component={NavLink} to="/login" sx={{ color: "white", textTransform: "None" }} >Login / Register</Button>
                    } */}
                </Toolbar>
            </AppBar>
        </Box>
    )
}

export default NavBar