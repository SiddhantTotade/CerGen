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

    const [participantData, setParticipantData] = useState({
        event_id: "",
        participant_name: "",
        participant_email: "",
        certificate_status: "",
    })

    function handleSubmit(e) {

        e.preventDefault();
        const url = 'http://127.0.0.1:8000/api/all-events/'
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
                    <TextField disabled onChange={(e) => handleEventData(e)} value={participantData.id} autoFocus margin="dense" id="event_id" label="Event Id" type="text" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} value={participantData.subject} autoFocus margin="dense" id="subject" label="Participant Name" type="text" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} value={participantData.from_date} autoFocus margin="dense" id="from_date" label="Participant Email" type="email" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} value={participantData.to_date} autoFocus margin="dense" id="to_date" label="Certificate Status" type="text" fullWidth variant="standard" />
                </DialogContent>
                <DialogActions>
                    <Button onClick={props.onClose}>Cancel</Button>
                    <Button onClick={handleSubmit} >Create Participant</Button>
                </DialogActions>
            </Dialog>
        </div>
    );
}