import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import axios from 'axios';
import { useState } from 'react';

export default function EventForm(props) {
    const [from_focus, from_setFocused] = React.useState(false)
    const [from_hasValue, from_setHasValue] = React.useState(false)
    const from_onFocus = () => from_setFocused(true)
    const from_onBlur = () => from_setFocused(false)

    const [to_focus, to_setFocused] = React.useState(false)
    const [to_hasValue, to_setHasValue] = React.useState(false)
    const to_onFocus = () => to_setFocused(true)
    const to_onBlur = () => to_setFocused(false)

    const [eventData, setEventData] = useState({
        event_name: "",
        subject: "",
        from_date: "",
        to_date: "",
    })

    function handleSubmit(e) {

        console.log(eventData);
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
                <DialogTitle>Add Event</DialogTitle>
                <DialogContent>
                    <TextField onChange={(e) => handleEventData(e)} value={eventData.event_name} autoFocus margin="dense" id="event_name" label="Event Name" type="text" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} value={eventData.subject} autoFocus margin="dense" id="subject" label="Event Subject" type="text" fullWidth variant="standard" />
                    <TextField onFocus={from_onFocus} onBlur={from_onBlur} onChange={(e) => { handleEventData(e); if (e.target.value) from_setHasValue(true); else from_setHasValue(false); }} type={from_hasValue || from_focus ? "date" : "text"} value={eventData.from_date} autoFocus margin="dense" id="from_date" label="Event From Date" fullWidth variant="standard" />
                    <TextField onFocus={to_onFocus} onBlur={to_onBlur} onChange={(e) => { handleEventData(e); if (e.target.value) to_setHasValue(true); else to_setHasValue(false); }} type={to_hasValue || to_focus ? 'date' : 'text'} value={eventData.to_date} autoFocus margin="dense" id="to_date" label="Event To Date" fullWidth variant="standard" />
                </DialogContent>
                <DialogActions>
                    <Button onClick={props.onClose}>Cancel</Button>
                    <Button onClick={handleSubmit} >Create Event</Button>
                </DialogActions>
            </Dialog>
        </div>
    );
}