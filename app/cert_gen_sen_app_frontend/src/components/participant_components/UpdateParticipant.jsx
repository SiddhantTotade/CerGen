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

    const [participantData, setParticipantData] = useState({
        event: "",
        student_name: "",
        email: "",
        certificate_status: "",
    })

    // participantData = props.participant

    useEffect(() => {
        participantData.event = props.participant.event
        participantData.student_name = props.participant.student_name
        participantData.email = props.participant.email
        participantData.certificate_status = props.participant.certificate_status
        // setParticipantData(props.participant)
    }, [props.participant])

    function handleSubmit(e) {

        e.preventDefault();
        const url = 'http://127.0.0.1:8000/api/update-participant/' + props.participant.event
        axios.put(url, {
            'event': participantData.event,
            'student_name': participantData.student_name,
            'email': participantData.email,
            'certificate_status': participantData.certificate_status,
        }).then(res => console.log(res)).catch(err => console.log(err))
    }

    console.log(participantData);

    function handleEventData(event) {

        const newData = { ...props.participant }
        newData[event.target.id] = event.target.value
        setParticipantData(newData)
    }


    return (
        <div className='w-full'>
            <Dialog {...props} >
                <DialogTitle>Add Participant</DialogTitle>
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