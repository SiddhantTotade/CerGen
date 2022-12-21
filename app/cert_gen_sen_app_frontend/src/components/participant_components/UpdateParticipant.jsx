import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import axios from 'axios';
import { useState, useEffect } from 'react';

export default function UpdateParticipant(props) {

    let [participantData, setParticipantData] = useState({})

    // useEffect(() => {
    //     setParticipantData(props.participant)
    // }, [props.participant])

    let [eventsData, setEventsData] = useState([])
    const event_url = window.location.href

    eventsData.map((event) => { return eventsData = event.id })

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
        const url = 'http://127.0.0.1:8000/api/update-participant/' + props.participant.event
        axios.put(url, {
            'event': eventsData,
            'student_name': participantData.student_name,
            'email': participantData.email,
            'certificate_status': participantData.certificate_status,
        }).then(res => console.log(res)).catch(err => console.log(err)).finally(props.onClose)
    }

    function handleEventData(event) {

        const newData = { ...props.participant }
        newData[event.target.id] = event.target.value
        setParticipantData(newData)
    }


    return (
        <div className='w-full'>
            <Dialog {...props} >
                <DialogTitle>Edit Participant</DialogTitle>
                <DialogContent>
                    <TextField disabled onChange={(e) => handleEventData(e)} defaultValue={props.participant.event} autoFocus margin="dense" id="event" label="Participant Id" type="text" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} defaultValue={props.participant.student_name} autoFocus margin="dense" id="student_name" label="Participant Name" type="text" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} defaultValue={props.participant.email} autoFocus margin="dense" id="email" label="Participant Email" type="email" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} defaultValue={props.participant.certificate_status} autoFocus margin="dense" id="certificate_status" label="Certificate Status" type="text" fullWidth variant="standard" />
                </DialogContent>
                <DialogActions>
                    <Button onClick={props.onClose} >Cancel</Button>
                    <Button onClick={handleSubmit} >Update Participant</Button>
                </DialogActions>
            </Dialog>
        </div>
    );
}