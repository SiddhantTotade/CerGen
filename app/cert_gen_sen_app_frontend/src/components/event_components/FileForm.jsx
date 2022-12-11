import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogTitle from '@mui/material/DialogTitle';
import Select from '@mui/material/Select';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import { useState, useEffect } from 'react';
import axios from 'axios';

export default function FileForm(props) {

    const [eventsData, setEventsData] = useState([])

    useEffect(() => {
        const url = 'http://127.0.0.1:8000/api/all-events/'

        const fetchData = async () => {
            try {
                const response = await axios.get(url)
                setEventsData(response.data)
            }
            catch (error) {
                console.log(error);
            }
        }
        fetchData()
    }, [])

    const [file_focus, file_setFocused] = React.useState(false)
    const [file_hasValue, file_setHasValue] = React.useState(false)
    const file_onFocus = () => file_setFocused(true)
    const file_onBlur = () => file_setFocused(false)

    const [events, setEvents] = React.useState('');

    const handleChange = (event) => {
        setEvents(event.target.value);
    };

    return (
        <div className='w-full'>
            <Dialog {...props} >
                <DialogTitle>Upload File</DialogTitle>
                <FormControl sx={{ minWidth: 400, margin: 2 }}>
                    <InputLabel id="events" >Events</InputLabel>
                    <Select
                        labelId="events"
                        id="demo-simple-select"
                        value={events}
                        label="Events"
                        onChange={handleChange}
                    >
                        {eventsData.map((events) => {
                            return <MenuItem value={events.id}>{events.event_name}</MenuItem>
                        })}
                    </Select>
                    <TextField onFocus={file_onFocus} onBlur={file_onBlur} onChange={(e) => { if (e.target.value) file_setHasValue(true); else file_setHasValue(false); }} type={file_hasValue || file_focus ? "file" : "file"} autoFocus margin="dense" id="event_name" label="File" fullWidth variant="standard" />
                </FormControl>
                <DialogActions>
                    <Button onClick={props.onClose}>Cancel</Button>
                    <Button >Upload File</Button>
                </DialogActions>
            </Dialog>
        </div >
    );
}