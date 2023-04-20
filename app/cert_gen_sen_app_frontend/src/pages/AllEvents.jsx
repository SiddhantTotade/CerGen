import React, { useState } from 'react'
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
import BackdropSpinner from '../components/base_components/Backdrop';
import AlertSnackbar from '../components/base_components/AlertSnackbar';

const card_sx = {
    maxWidth: 400,
    transition: 'all 0.25s ease-in-out',
    display: "grid",
    '&:hover': {
        background: "#f3f3f3",
    }
}

const card = 6

const cardSkeleton = [...Array(card)].map((e, i) =>
    <Card key={i} >
        <CardContent>
            <div>
                <Typography gutterBottom variant="h5" component="div">
                    <LoaderSkeleton />
                </Typography>
                <div className='flex flex-col'>
                    <div>
                        <LoaderSkeleton />
                        <LoaderSkeleton barWidth={100} />
                    </div>
                </div>
                <br />
            </div>
            <Typography variant='h1'>
                <LoaderSkeleton />
            </Typography>
        </CardContent>
    </Card>
)

export const AllEvents = () => {

    const [snackAndSpinner, setSnackAndSpinner] = useState({
        openSpinner: true,
        openSnack: true,
        message: "",
        alertType: "success"
    })

    const { access_token } = getToken()

    const { data = [], isLoading } = useGetAllEventsQuery(access_token)

    const [deleteEvent, responseDeleteEvent] = useDeleteEventMutation()

    let days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

    function handleCloseSnackbar() {
        setSnackAndSpinner({ openSnack: false });
    }

    return (
        <>
            <Sidebar />
            <Typography sx={{ display: "flex", justifyContent: "center", fontSize: "30px", borderBottom: "1px solid gray", width: "55%", margin: "auto" }}>All Events</Typography>
            {
                isLoading ?
                    <div className='grid gap-5 justify-center col-auto grid-cols-3 p-10 w-3/5 m-auto'>
                        {
                            cardSkeleton
                        }
                    </div>
                    :
                    <>
                        {
                            responseDeleteEvent.isLoading ? <BackdropSpinner open={snackAndSpinner.openSpinner} /> :
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
                                                    {event.subject.length > 100 ? event.subject.substring(0, 85) + "....." : event.subject}
                                                </Typography>
                                            </CardContent>
                                            <CardActions>
                                                <Button variant='contained' size="small"><Link sx={{ textDecoration: 'none' }} to={event_url}>View</Link></Button>
                                                <Button variant='contained' size="small" onClick={() => deleteEvent({ access_token: access_token, slug: event.slug })} >Delete</Button>
                                            </CardActions>
                                        </Card>

                                    }) : <h2>No Data Available</h2>}
                                    {
                                        responseDeleteEvent.data ? <AlertSnackbar
                                            open={snackAndSpinner.openSnack}
                                            message={responseDeleteEvent.data}
                                            severity={snackAndSpinner.alertType}
                                            onClose={handleCloseSnackbar}
                                            autoHideDuration={6000}
                                        /> : ""
                                    }
                                </div>
                        }

                    </>
            }
        </>
    )
}
