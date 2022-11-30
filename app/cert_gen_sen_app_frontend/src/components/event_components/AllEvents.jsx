import React from 'react'
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { Link } from '@mui/material';
import Sidebar from "../base_components/Sidebar";

const card_sx = {
    maxWidth: 345,
    cursor: 'pointer'
}

export const AllEvents = () => {
    return (
        <>
            <Sidebar />
            <div className='grid gap-5 justify-center col-auto grid-cols-3 p-10 w-3/5 m-auto' >
                <Card sx={card_sx}>
                    <CardContent>
                        <div className='flex items-center justify-between'>
                            <Typography gutterBottom variant="h5" component="div">
                                Lizard
                            </Typography>
                            <div>
                                <small>Date</small>
                            </div>
                        </div>
                        <Typography variant="body2" color="text.secondary">
                            Lizards are a widespread group of squamate reptiles, with over 6,000
                            species, ranging across all continents except Antarctica
                        </Typography>
                    </CardContent>
                    <CardActions>
                        <Button size="small"><Link sx={{ textDecoration: 'none' }}>View</Link></Button>
                        <Button size="small"><Link sx={{ textDecoration: 'none' }}>Delete</Link></Button>
                    </CardActions>
                </Card>
            </div>
        </>
    )
}
