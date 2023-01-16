import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import axios from 'axios';
import { useState, useEffect } from 'react';
import AlertSnackbar from '../base_components/AlertSnackbar';
import BackdropSpinner from '../base_components/Backdrop';

export default function CreateParticipant(props) {

    const [openSnack, setOpenSnack] = useState(false)
    const [message, setMessage] = useState("")
    const [alertType, setAlertType] = useState("")
    const [openSpinner, setOpenSpinner] = useState(false)

    const [participantData, setParticipantData] = useState({
        event: "",
        student_name: "",
        student_id: "",
        email: "",
        certificate_status: "",
    })

    const [eventsData, setEventsData] = useState([])
    const event_url = window.location.href

    eventsData.map((event) => { return participantData.event = event.id })

    useEffect(() => {

        const new_event_url = event_url.replace("3000", "8000").replace("event", "event-details")

        const fetchData = async () => {
            try {
                const response = await axios.get(new_event_url)
                setEventsData(response.data)
            }
            catch (error) {
                console.log(error);
            }
        }
        fetchData()
    }, [event_url])

    function handleSubmit(e) {
        e.preventDefault();
        setOpenSpinner(true)
        setTimeout(() => { setOpenSpinner(false) }, 5000)
        const url = 'http://127.0.0.1:8000/api/create-participant/'
        axios.post(url, {
            'event': participantData.event,
            'student_name': participantData.student_name,
            'student_id': participantData.student_id,
            'email': participantData.email,
            'certificate_status': participantData.certificate_status,
        }).then(setTimeout(() => { setOpenSnack(true) }, 5000)).then(res => setMessage(res.data)).then(message === "Participant added successfully" ? setAlertType("error") : setAlertType("success")).catch(err => console.log(err)).finally(props.onClose)
    }

    function handleEventData(event) {

        const newData = { ...participantData }
        newData[event.target.id] = event.target.value
        setParticipantData(newData)
    }

    function handleCloseSnackbar() {
        setOpenSnack(false)
    }

    return (
        <div className='w-full'>
            <Dialog {...props} >
                <DialogTitle>Add Participant</DialogTitle>
                <DialogContent>
                    <TextField disabled onChange={(e) => handleEventData(e)} value={participantData.event} autoFocus margin="dense" id="event" label="Event Id" type="text" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} value={participantData.student_name} autoFocus margin="dense" id="student_name" label="Participant Name" type="text" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} value={participantData.student_id} autoFocus margin="dense" id="student_id" label="Participant Id" type="text" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} value={participantData.email} autoFocus margin="dense" id="email" label="Participant Email" type="email" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} value={participantData.certificate_status} autoFocus margin="dense" id="certificate_status" label="Certificate Status" type="text" fullWidth variant="standard" />
                </DialogContent>
                <DialogActions>
                    <Button onClick={props.onClose} >Cancel</Button>
                    <Button onClick={handleSubmit} >Create Participant</Button>
                </DialogActions>
            </Dialog>
            <BackdropSpinner open={openSpinner} />
            <AlertSnackbar open={openSnack} message={message} severity={alertType} onClose={handleCloseSnackbar} autoHideDuration={6000} />
        </div>
    );
}