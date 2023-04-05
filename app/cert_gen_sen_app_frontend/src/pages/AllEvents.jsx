import React from 'react'
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { Link } from 'react-router-dom';
import Sidebar from "../components/base_components/Sidebar";
import { useState, useEffect } from 'react';
import axios from 'axios'
import BackdropSpinner from '../components/base_components/Backdrop';
import AlertSnackbar from '../components/base_components/AlertSnackbar';
import { useGetAllEventsQuery } from '../services/eventsAPI';
import { useDispatch, useSelector } from 'react-redux';
import { getToken } from '../services/LocalStorageService';

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

export const AllEvents = () => {

    const [eventsData, setEventsData] = useState([])
    const [openSnack, setOpenSnack] = useState(false)
    const [message, setMessage] = useState("")
    const [alertType, setAlertType] = useState("")
    const [openSpinner, setOpenSpinner] = useState(false)

    const dispatch = useDispatch()
    const { access_token } = getToken()
    const { data, isSuccess } = useGetAllEventsQuery(access_token)

    let days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

    useEffect(() => {
        if (data && isSuccess) {
            dispatch()
        }
        // const url = 'http://127.0.0.1:8000/api/all-events/'

        // const fetchData = async () => {
        //     try {
        //         const response = await axios.get(url, { headers: { "authorization": "Bearer " + localStorage.getItem("access_token") } })
        //         setEventsData(response.data)
        //     }
        //     catch (error) {
        //         console.log(error);
        //     }
        // }
        // fetchData()
    }, [data, isSuccess, dispatch])

    function handleDelete(event_slug) {
        setOpenSpinner(true)
        setTimeout(() => { setOpenSpinner(false) }, 2000)
        const url = 'http://127.0.0.1:8000/api/event/' + event_slug
        axios.delete(url, { headers: { "Authorization": "Token " + localStorage.getItem("token") } }).then(setTimeout(() => { setOpenSnack(true) }, 2000)).then(res => setMessage(res.data)).then(message === "Event added successfully" ? setAlertType("error") : setAlertType("success")).catch(err => console.log(err))
    }

    function handleCloseSnackbar() {
        setOpenSnack(false)
    }

    return (
        <>
            <Sidebar />
            <Typography sx={{ display: "flex", justifyContent: "center", fontSize: "30px", borderBottom: "1px solid gray", width: "55%", margin: "auto" }}>All Events</Typography>
            <div className='grid gap-5 justify-center col-auto grid-cols-3 p-10 w-3/5 m-auto' >
                {eventsData !== 'No event data' ? eventsData.map((event) => {
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
                            <Button size="small" onClick={() => handleDelete(event.slug)} >Delete</Button>
                        </CardActions>
                    </Card>
                }) : <h2>No Data Available</h2>}
            </div>
            <BackdropSpinner open={openSpinner} />
            <AlertSnackbar open={openSnack} message={message} severity={alertType} onClose={handleCloseSnackbar} autoHideDuration={6000} />
        </>
    )
}
