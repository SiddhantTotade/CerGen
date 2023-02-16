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
import BackdropSpinner from '../base_components/Backdrop';
import AlertSnackbar from '../base_components/AlertSnackbar';

export default function FileForm(props) {

    const [eventsData, setEventsData] = useState([])
    const [openSpinner, setOpenSpinner] = useState(false)
    const [openSnack, setOpenSnack] = useState(false)
    const [message, setMessage] = useState("")
    const [alertType, setAlertType] = useState("")

    useEffect(() => {
        const url = 'http://127.0.0.1:8000/api/all-events/'

        const fetchData = async () => {
            try {
                const response = await axios.get(url, { headers: { "Authorization": "Token " + localStorage.getItem("token") } })
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
    const [eventId, setEventId] = React.useState('');
    const [eventFileData, setEventFileData] = React.useState({
        eventID: "",
        eventFile: null
    })

    const handleChange = (event) => {
        setEvents(event.target.value);
        setEventId(event.target.value)
    };

    function handleFileChange(event) {
        setEventFileData(event.target.files[0])
    }

    function handleFileSubmit(event) {

        event.preventDefault();
        setOpenSpinner(true)
        setTimeout(() => { setOpenSpinner(false) }, 5000)
        const formData = new FormData()
        formData.append('xlsx_file', eventFileData)
        formData.append('eventId', eventId)
        const url = 'http://127.0.0.1:8000/api/upload-participants/'
        const config = {
            headers: {
                'content-type': 'multipart/form-data',
                "Authorization": "Token " + localStorage.getItem("token")
            }
        }
        axios.post(url, formData, config).then(setTimeout(() => { setOpenSnack(true) }, 5000)).then(res => setMessage(res.data)).then(message === "Participants uploaded successfully" ? setAlertType("error") : setAlertType("success")).catch(err => console.log(err)).finally(props.onClose)
    }

    function handleCloseSnackbar() {
        setOpenSnack(false)
    }

    return (
        <div className='w-full'>
            <Dialog {...props} >
                <DialogTitle>Upload File</DialogTitle>
                <FormControl sx={{ minWidth: 400, margin: 2 }}>
                    <InputLabel id="events" >Choose Event</InputLabel>
                    <Select labelId="events" id="event_dropdown" value={events} variant="standard" label="Events" onChange={handleChange} >
                        {eventsData !== undefined ? Object.values(eventsData).map((events) => {
                            return <MenuItem value={events.id} key={events} >{events.event_name}</MenuItem>
                        }) : <MenuItem value={events.id} key={events.id}>No Data Available</MenuItem>}
                    </Select>
                    <TextField onFocus={file_onFocus} onBlur={file_onBlur} onChange={(e) => { handleFileChange(e); if (e.target.value) file_setHasValue(true); else file_setHasValue(false); }} type={file_hasValue || file_focus ? "file" : "file"} autoFocus margin="dense" id="xlsx_file" label="File" fullWidth variant="standard" />
                </FormControl>
                <DialogActions>
                    <Button onClick={props.onClose}>Cancel</Button>
                    <Button onClick={handleFileSubmit} >Upload File</Button>
                </DialogActions>
            </Dialog>
            <BackdropSpinner open={openSpinner} />
            <AlertSnackbar open={openSnack} message={message} severity={alertType} onClose={handleCloseSnackbar} autoHideDuration={6000} />
        </div >
    );
}