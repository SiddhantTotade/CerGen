import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import { useState } from 'react';
import { Select } from '@mui/material';
import AlertSnackbar from '../base_components/AlertSnackbar';
import BackdropSpinner from '../base_components/Backdrop';
import { useCreateEventMutation } from '../../services/eventsAPI';
import { getToken } from '../../services/LocalStorageService';
import { useGetLoggedInUserQuery } from '../../services/userAuthAPI';
import { useDispatch } from 'react-redux';
import { setUserInfo } from '../../features/userSlice';
import { useSelector } from 'react-redux';

export default function EventForm(props) {
    const [openSnack, setOpenSnack] = useState(false)
    const [message, setMessage] = useState("")
    const [alertType, setAlertType] = useState("")
    const [openSpinner, setOpenSpinner] = useState(false)

    const [from_focus, from_setFocused] = React.useState(false)
    const [from_hasValue, from_setHasValue] = React.useState(false)
    const from_onFocus = () => from_setFocused(true)
    const from_onBlur = () => from_setFocused(false)

    const [to_focus, to_setFocused] = React.useState(false)
    const [to_hasValue, to_setHasValue] = React.useState(false)
    const to_onFocus = () => to_setFocused(true)
    const to_onBlur = () => to_setFocused(false)

    const { access_token } = getToken()

    const { data = [], isSuccess } = useGetLoggedInUserQuery(access_token)

    const dispatch = useDispatch()

    React.useEffect(() => {
        if (data && isSuccess) {
            dispatch(setUserInfo({ email: data.email, name: data.name }))
        }
    }, [data, isSuccess, dispatch])

    const [eventData, setEventData] = useState({
        user: data.id,
        event_name: "",
        subject: "",
        event_department: "",
        from_date: "",
        to_date: "",
        event_year: "",
    })

    const [createEvent, responseCreateEvent] = useCreateEventMutation()

    const [eventYear, setEventYear] = useState("")

    function handleEventData(event) {
        const newData = { ...eventData }
        newData[event.target.id] = event.target.value
        setEventData(newData)
    }

    const handleEventYear = (event) => {
        setEventYear(event.target.value)
        eventData.event_year = event.target.value
    }

    let maxOffset = 10;
    let thisYear = (new Date()).getFullYear();
    let allYears = [];
    for (let x = 0; x <= maxOffset; x++) {
        allYears.push(thisYear - x)
    }

    const yearList = allYears.map((x) => { return <MenuItem value={x} key={x}>{x}</MenuItem> });

    function handleCloseSnackbar() {
        setOpenSnack(false)
    }

    return (
        <div className='w-full'>
            <Dialog {...props} >
                <DialogTitle>Create Event</DialogTitle>
                <DialogContent>
                    <TextField onChange={(e) => handleEventData(e)} value={eventData.event_name} autoFocus margin="dense" id="event_name" label="Event Name" type="text" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} value={eventData.subject} autoFocus margin="dense" id="subject" label="Event Subject" type="text" fullWidth variant="standard" />
                    <TextField onChange={(e) => handleEventData(e)} value={eventData.event_department} autoFocus margin="dense" id="event_department" label="Event Department" type="text" fullWidth variant="standard" />
                    <TextField onFocus={from_onFocus} onBlur={from_onBlur} onChange={(e) => { handleEventData(e); if (e.target.value) from_setHasValue(true); else from_setHasValue(false); }} type={from_hasValue || from_focus ? "date" : "text"} value={eventData.from_date} autoFocus margin="dense" id="from_date" label="Event - From Date" fullWidth variant="standard" />
                    <TextField onFocus={to_onFocus} onBlur={to_onBlur} onChange={(e) => { handleEventData(e); if (e.target.value) to_setHasValue(true); else to_setHasValue(false); }} type={to_hasValue || to_focus ? 'date' : 'text'} value={eventData.to_date} autoFocus margin="dense" id="to_date" label="Event - To Date" fullWidth variant="standard" />
                    <FormControl variant="standard" sx={{ width: "100%" }}  >
                        <InputLabel id="demo-simple-select-label" variant='standard' >Choose Event Year</InputLabel>
                        <Select labelId="demo-simple-select-label" id="demo-simple-select" variant="standard" onChange={handleEventYear} value={eventYear}>
                            <MenuItem value="" key="" >
                                <em>None</em>
                            </MenuItem>
                            {yearList}
                        </Select>
                    </FormControl>
                </DialogContent>
                <DialogActions>
                    <Button variant='contained' onClick={props.onClose}>Cancel</Button>
                    <Button variant='contained' onClick={() => createEvent({ access_token: access_token, eventData: eventData })} >Create</Button>
                </DialogActions>
            </Dialog>
            <BackdropSpinner open={openSpinner} />
            <AlertSnackbar open={openSnack} message={message} severity={alertType} onClose={handleCloseSnackbar} autoHideDuration={6000} />
        </div>
    );
}