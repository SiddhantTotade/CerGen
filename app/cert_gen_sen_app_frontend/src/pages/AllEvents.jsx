import React, { useState } from 'react'
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { Link } from 'react-router-dom';
import Sidebar from "../components/base_components/Sidebar";
import { useGetAllEventsQuery } from '../services/eventsAPI';
import { getToken } from '../services/LocalStorageService';
import LoaderSkeleton from '../components/base_components/LoaderSkeleton';
import UpdateEvent from '../components/event_components/UpdateEvent';
import DeleteEvent from '../components/event_components/DeleteEvent';

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

    const [eventData, setEventData] = useState({
        id: "",
        event_name: "",
        subject: "",
        event_department: "",
        from_date: "",
        to_date: "",
        event_year: "",
        slug: "",
    })

    const { access_token } = getToken()

    const { data = [], isLoading } = useGetAllEventsQuery(access_token)

    let days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

    const [updateForm, setUpdateForm] = useState(false);

    const [deleteForm, setDeleteForm] = useState(false);

    const handleUpdateForm = (id, event_name, subject, event_department, from_date, to_date, event_year, slug) => {
        setUpdateForm(true)
        setEventData({ id: id, event_name: event_name, subject: subject, event_department: event_department, from_date: from_date, to_date: to_date, event_year: event_year, slug: slug })
    }

    const handleUpdateFormClose = () => {
        setUpdateForm(false)
    }

    const handleDeleteForm = (id, event_name, subject, event_department, from_date, to_date, event_year, slug) => {
        setDeleteForm(true)
        setEventData({ id: id, event_name: event_name, subject: subject, event_department: event_department, from_date: from_date, to_date: to_date, event_year: event_year, slug: slug })
    }

    const handleDeleteFormClose = () => {
        setDeleteForm(false)
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
                                        <Button variant='contained' size="small" onClick={() => handleUpdateForm(event.id, event.event_name, event.subject, event.event_department, event.from_date, event.to_date, event.event_year, event.slug)}>Edit</Button>
                                        <Button variant='contained' size="small" onClick={() => handleDeleteForm(event.id, event.event_name, event.subject, event.event_department, event.from_date, event.to_date, event.event_year, event.slug)} >Delete</Button>
                                    </CardActions>
                                </Card>

                            }) : <h2>No Data Available</h2>}
                        </div>
                    </>
            }
            <UpdateEvent open={updateForm} onClose={handleUpdateFormClose} event={eventData} />
            <DeleteEvent open={deleteForm} onClose={handleDeleteFormClose} event={eventData} />
        </>
    )
}
