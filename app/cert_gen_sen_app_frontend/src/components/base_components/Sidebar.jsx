import * as React from 'react';
import Box from '@mui/material/Box';
import SwipeableDrawer from '@mui/material/SwipeableDrawer';
import List from '@mui/material/List';
import Divider from '@mui/material/Divider';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import CloudUploadOutlinedIcon from '@mui/icons-material/CloudUploadOutlined';
import AccountBoxOutlinedIcon from '@mui/icons-material/AccountBoxOutlined';
import Logout from '@mui/icons-material/Logout';
import CloseOutlinedIcon from '@mui/icons-material/CloseOutlined';
import { Component } from 'react';
import { Link } from 'react-router-dom';


export default class Sidebar extends Component {

    render() {

        return (
            <div>
                <React.Fragment >
                    <SwipeableDrawer {...this.props}>
                        <Box sx={{ width: '300px' }} role="presentation">
                            <div className='absolute right-5 p-1 cursor-pointer'>
                                <List>
                                    <ListItem onClick={this.props.onClose} disablePadding>
                                        <CloseOutlinedIcon />
                                    </ListItem>
                                </List>
                            </div>
                            <div className='flex justify-center mt-16'>
                                <Link to='/' className='font-title text-sky-600 underline underline-offset-4 decoration-slate-400 text-xl tracking-widest'>MARTLE</Link>
                            </div>
                            <List>
                                <ListItem className='mt-16' disablePadding>
                                    <ListItemButton>
                                        <ListItemIcon><AccountBoxOutlinedIcon /></ListItemIcon>
                                        <ListItemText primary="Your Account" />
                                    </ListItemButton>
                                </ListItem>
                            </List>
                            <List>
                                <Link to='/api/product-upload' >
                                    <ListItem disablePadding>
                                        <ListItemButton>
                                            <ListItemIcon><CloudUploadOutlinedIcon /></ListItemIcon>
                                            <ListItemText primary="Upload Product" />
                                        </ListItemButton>
                                    </ListItem>
                                </Link>
                            </List>
                            <Divider />
                            <List>
                                <ListItem disablePadding>
                                    <ListItemButton>
                                        <ListItemIcon><Logout /></ListItemIcon>
                                        <ListItemText primary="Logout" />
                                    </ListItemButton>
                                </ListItem>
                            </List>
                        </Box>
                    </SwipeableDrawer>
                </React.Fragment>
            </div>
        );
    }
}