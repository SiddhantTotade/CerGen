import React from 'react'
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { Link } from 'react-router-dom';
import Sidebar from "../base_components/Sidebar";
import { useState, useEffect } from 'react';
import axios from 'axios'

const card_sx = {
    maxWidth: 345,
    transition: 'all 0.25s ease-in-out',
    cursor: 'pointer',
    '&:hover': {
        background: "#fcfcfa",
        transform: 'scale(1.1)',
        transition: 'all 0.25s ease-in-out'
    }
}

export const AllEvents = () => {

    const [eventsData, setEventsData] = useState([])

    useEffect(() => {
        const url = 'http://127.0.0.1:8000/api/all-events/'

        const fetchData = async () => {
            try {
                const response = await axios.get(url)
                setEventsData(response.data)
            }
            catch (error) {
                console.log(error);
            }
        }
        fetchData()
    }, [])

    return (
        <>
            <Sidebar />
            <div className='grid gap-5 justify-center col-auto grid-cols-3 p-10 w-3/5 m-auto' >
                {eventsData.map((event) => {
                    return <Link to={event.slug}>
                        <Card sx={card_sx}>
                            <CardContent>
                                <div className='flex items-center justify-between'>
                                    <Typography gutterBottom variant="h5" component="div">
                                        {event.event_name}
                                    </Typography>
                                    <div>
                                        <small>{event.from_date} - {event.to_date}</small>
                                    </div>
                                </div>
                                <Typography variant="body2" color="text.secondary">
                                    Lizards are a widespread group of squamate reptiles, with over 6,000
                                    species, ranging across all continents except Antarctica
                                </Typography>
                            </CardContent>
                            <CardActions>
                                <Button size="small"><Link sx={{ textDecoration: 'none' }} to={event.slug}>View</Link></Button>
                                <Button size="small"><Link sx={{ textDecoration: 'none' }} to={event.slug}>Delete</Link></Button>
                            </CardActions>
                        </Card>
                    </Link>
                })}
            </div>
        </>
    )
}
