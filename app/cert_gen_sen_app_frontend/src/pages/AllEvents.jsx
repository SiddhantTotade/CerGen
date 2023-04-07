import React from 'react'
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { Link } from 'react-router-dom';
import Sidebar from "../components/base_components/Sidebar";
import { useGetAllEventsQuery, useDeleteEventMutation } from '../services/eventsAPI';
import { getToken } from '../services/LocalStorageService';
import LoaderSkeleton from '../components/base_components/LoaderSkeleton';

const card_sx = {
    maxWidth: 400,
    transition: 'all 0.25s ease-in-out',
    display: "grid",
    '&:hover': {
        background: "#fcfcfa",
        transform: 'scale(1.1)',
        transition: 'all 0.25s ease-in-out'
    }
}

const CardSkeleton =
    <div className='grid gap-5 justify-center col-auto grid-cols-3 w-3/6' >
        <Card >
            <CardContent>
                <div>
                    <Typography gutterBottom variant="h5" component="div">
                        <LoaderSkeleton />
                    </Typography>
                    <div className='flex flex-col'>
                        <div>
                            <LoaderSkeleton />
                            <LoaderSkeleton />
                        </div>
                        <LoaderSkeleton />
                    </div>
                    <br />
                </div>
                <LoaderSkeleton barPadding={5} />
            </CardContent>
        </Card>
    </div>

export const AllEvents = () => {

    const card = 6

    const { access_token } = getToken()

    const { data = [], isLoading } = useGetAllEventsQuery(access_token)

    const [deleteEvent, responseDeleteEvent] = useDeleteEventMutation()

    let days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

    return (
        <>
            <Sidebar />
            <Typography sx={{ display: "flex", justifyContent: "center", fontSize: "30px", borderBottom: "1px solid gray", width: "55%", margin: "auto" }}>All Events</Typography>
            {
                isLoading ?
                    [...Array(card)].map((e, i) =>
                        <div key={i} className='grid gap-5 justify-center col-auto grid-cols-3 p-10 w-3/5 m-auto'>
                            {
                                CardSkeleton
                            }
                        </div>
                    )
                    :
                    <div className='grid gap-5 justify-center col-auto grid-cols-3 p-10 w-3/5 m-auto' >
                        {data !== 'No event data' ? data.map((event) => {
                            let event_url = '/api/event/' + event.slug
                            return <Card sx={card_sx} key={event.id} >
                                <CardContent>
                                    <div>
                                        <Typography gutterBottom variant="h5" component="div">
                                            {event.event_name}
                                        </Typography>
                                        <div className='flex flex-col'>
                                            <div>
                                                <small>{days[new Date(event.from_date).getDay()]}</small>
                                                {event.from_date !== event.to_date ? <small> - {days[new Date(event.to_date).getDay()]}</small> : ""}
                                            </div>
                                            <small>{new Date(event.from_date).toLocaleDateString('en-GB')} - {new Date(event.to_date).toLocaleDateString('en-GB')}</small>
                                        </div>
                                        <br />
                                    </div>
                                    <Typography variant="body2" color="text.secondary" sx={{ height: "5vh" }}>
                                        {event.subject}
                                    </Typography>
                                </CardContent>
                                <CardActions>
                                    <Button size="small"><Link sx={{ textDecoration: 'none' }} to={event_url}>View</Link></Button>
                                    <Button size="small" onClick={() => deleteEvent({ access_token: access_token, slug: event.slug })} >Delete</Button>
                                </CardActions>
                            </Card>
                        }) : <h2>No Data Available</h2>}
                    </div>
            }
        </>
    )
}
