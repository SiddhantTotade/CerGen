import React from 'react'
import NavBar from '../components/base_components/NavBar'
import { Outlet } from 'react-router-dom'
import { CssBaseline } from '@mui/material'

const Layout = () => {
    return (
        <>
            <CssBaseline />
            <NavBar />
            <Outlet />
        </>
    )
}

export default Layout