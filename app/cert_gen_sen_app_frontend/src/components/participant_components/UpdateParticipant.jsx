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

export default function UpdateParticipant(props) {

    let [eventsData, setEventsData] = useState([])

    Object.values(eventsData).map((event) => { return eventsData = event.id })

    const [participantData, setParticipantData] = useState({
        event: "",
        student_name: "",
        student_id: "",
        email: "",
        certificate_status: ""
    })

    const [updateParticipantData, setUpdateParticipantData] = useState({
        event: "",
        student_name: "",
        student_id: "",
        email: "",
        certificate_status: ""
    })

    const [openSnack, setOpenSnack] = useState(false)
    const [message, setMessage] = useState("")
    const [alertType, setAlertType] = useState("")

    useEffect(() => {
        const event_url = window.location.href
        const new_event_url = event_url.replace("3000", "8000").replace("event", "event-details")
        axios.get(new_event_url).then(res => setEventsData(res.data))
    }, [])

    useEffect(() => {
        settingParticipantData()
        // eslint-disable-next-line
    }, [])

    function handleSubmit(e) {
        e.preventDefault();
        const url = 'http://127.0.0.1:8000/api/update-participant/' + props.participant.event
        axios.put(url, {
            'event': eventsData,
            'student_name': updateParticipantData.student_name === "" ? participantData.student_name : updateParticipantData.student_name,
            'student_id': updateParticipantData.student_id === "" ? participantData.student_id : updateParticipantData.student_id,
            'email': updateParticipantData.email === "" ? participantData.email : updateParticipantData.email,
            'certificate_status': updateParticipantData.certificate_status === "" ? participantData.certificate_status : updateParticipantData.certificate_status,
        }).then(setOpenSnack(true)).then(res => setMessage(res.data)).then(message === "Participant updated successfully" ? setAlertType("success") : setAlertType("error")).catch(err => console.log(err)).finally(props.onClose)
    }

    // function handleSeverity(msg) {
    //     message.message = msg
    // }

    console.log(message);

    function handleEventData(event) {

        const newData = { ...updateParticipantData }
        newData[event.target.id] = event.target.value
        setUpdateParticipantData(newData)
    }

    function settingParticipantData() {
        setParticipantData(props.participant)
    }

    function handleCloseSnackbar() {
        setOpenSnack(false)
    }

    return (
        <div className='w-full'>
            <Dialog {...props} >
                <DialogTitle>Edit Participant</DialogTitle>
                <DialogContent>
                    <TextField disabled defaultValue={props.participant.event} autoFocus margin="dense" id="event" label="Participant Id" type="text" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} defaultValue={props.participant.student_name} autoFocus margin="dense" id="student_name" label="Participant Name" type="text" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} defaultValue={props.participant.student_id} autoFocus margin="dense" id="student_id" label="Participant Id" type="text" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} defaultValue={props.participant.email} autoFocus margin="dense" id="email" label="Participant Email" type="email" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} defaultValue={props.participant.certificate_status} autoFocus margin="dense" id="certificate_status" label="Certificate Status" type="text" fullWidth variant="standard" />
                </DialogContent>
                <DialogActions>
                    <Button onClick={props.onClose} >Cancel</Button>
                    <Button onClick={handleSubmit} >Update Participant</Button>
                </DialogActions>
            </Dialog>
            <AlertSnackbar open={openSnack} message={message} severity={alertType} onClose={handleCloseSnackbar} autoHideDuration={6000} />
        </div>
    );
}