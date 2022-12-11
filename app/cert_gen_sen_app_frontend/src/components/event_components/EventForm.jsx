import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import axios from 'axios';

export default function EventForm(props) {
    const [from_focus, from_setFocused] = React.useState(false)
    const [from_hasValue, from_setHasValue] = React.useState(false)
    const from_onFocus = () => from_setFocused(true)
    const from_onBlur = () => from_setFocused(false)

    const [to_focus, to_setFocused] = React.useState(false)
    const [to_hasValue, to_setHasValue] = React.useState(false)
    const to_onFocus = () => to_setFocused(true)
    const to_onBlur = () => to_setFocused(false)

    function handleEventData() {

        const url = 'http://127.0.0.1:8000/api/all-events/'
        axios.post(url, {
            'event_name': this.state.event_name,
            'subject': this.state.event_subject,
            'from_date': this.state.event_from_date,
            'to_date': this.state.event_to_date
        }, {
            headers: {
                'Content-Type': 'application/json',
            }
        }
        ).then(res => console.log(res)).catch(err => console.log(err))
    }

    return (
        <div className='w-full'>
            <Dialog {...props} >
                <DialogTitle>Add Event</DialogTitle>
                <DialogContent>
                    <TextField autoFocus margin="dense" id="event_name" label="Event Name" type="text" fullWidth variant="standard" />
                    <TextField autoFocus margin="dense" id="event_subject" label="Event Subject" type="text" fullWidth variant="standard" />
                    <TextField onFocus={from_onFocus} onBlur={from_onBlur} onChange={(e) => { if (e.target.value) from_setHasValue(true); else from_setHasValue(false); }} type={from_hasValue || from_focus ? "date" : "text"} autoFocus margin="dense" id="event_from_date" label="Event From Date" fullWidth variant="standard" />
                    <TextField onFocus={to_onFocus} onBlur={to_onBlur} onChange={(e) => { if (e.target.value) to_setHasValue(true); else to_setHasValue(false); }} type={to_hasValue || to_focus ? 'date' : 'text'} autoFocus margin="dense" id="event_to_date" label="Event To Date" fullWidth variant="standard" />
                </DialogContent>
                <DialogActions>
                    <Button onClick={props.onClose}>Cancel</Button>
                    <Button onClick={handleEventData} >Create Event</Button>
                </DialogActions>
            </Dialog>
        </div>
    );
}