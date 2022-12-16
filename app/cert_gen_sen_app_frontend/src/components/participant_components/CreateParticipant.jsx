import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import axios from 'axios';
import { useState } from 'react';

export default function CreateParticipant(props) {

    const [eventData, setEventData] = useState({
        event_name: "",
        subject: "",
        from_date: "",
        to_date: "",
    })

    function handleSubmit(e) {

        e.preventDefault();
        const url = 'http://127.0.0.1:8000/api/all-events/'
        axios.post(url, {
            'user': 1,
            'event_name': eventData.event_name,
            'subject': eventData.subject,
            'from_date': eventData.from_date,
            'to_date': eventData.to_date,
        }).then(res => console.log(res)).catch(err => console.log(err))
    }

    function handleEventData(event) {

        const newData = { ...eventData }
        newData[event.target.id] = event.target.value
        setEventData(newData)
    }

    return (
        <div className='w-full'>
            <Dialog {...props} >
                <DialogTitle>Add Participant</DialogTitle>
                <DialogContent>
                    <TextField disabled onChange={(e) => handleEventData(e)} value={eventData.id} autoFocus margin="dense" id="event_id" label="Event Id" type="text" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} value={eventData.subject} autoFocus margin="dense" id="subject" label="Participant Name" type="text" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} value={eventData.from_date} autoFocus margin="dense" id="from_date" label="Participant Email" type="text" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} value={eventData.to_date} autoFocus margin="dense" id="to_date" label="Certificate Status" type="text" fullWidth variant="standard" />
                </DialogContent>
                <DialogActions>
                    <Button onClick={props.onClose}>Cancel</Button>
                    <Button onClick={handleSubmit} >Create Participant</Button>
                </DialogActions>
            </Dialog>
        </div>
    );
}