import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import axios from 'axios';
import { useState, useEffect } from 'react';

export default function CreateParticipant(props) {

    const [participantData, setParticipantData] = useState({
        event_id: "",
        participant_name: "",
        participant_email: "",
        certificate_status: "",
    })

    const [eventsData, setEventsData] = useState([])
    const event_url = window.location.href

    eventsData.map((event) => { return participantData.event_id = event.id })

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
        const url = 'http://127.0.0.1:8000/api/create-participant/'
        axios.post(url, {
            'event_id': participantData,
            'participant_name': participantData.event_name,
            'participant_email': participantData.subject,
            'certificate_status': participantData.from_date,
        }).then(res => console.log(res)).catch(err => console.log(err))
    }

    function handleEventData(event) {

        const newData = { ...participantData }
        newData[event.target.id] = event.target.value
        setParticipantData(newData)
    }

    return (
        <div className='w-full'>
            <Dialog {...props} >
                <DialogTitle>Add Participant</DialogTitle>
                <DialogContent>
                    <TextField disabled onChange={(e) => handleEventData(e)} value={participantData.event_id} autoFocus margin="dense" id="event_id" label="Event Id" type="text" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} value={participantData.participant_name} autoFocus margin="dense" id="participant_name" label="Participant Name" type="text" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} value={participantData.participant_email} autoFocus margin="dense" id="participant_email" label="Participant Email" type="email" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} value={participantData.certificate_status} autoFocus margin="dense" id="certificate_status" label="Certificate Status" type="text" fullWidth variant="standard" />
                </DialogContent>
                <DialogActions>
                    <Button onClick={props.onClose}>Cancel</Button>
                    <Button onClick={handleSubmit} >Create Participant</Button>
                </DialogActions>
            </Dialog>
        </div>
    );
}