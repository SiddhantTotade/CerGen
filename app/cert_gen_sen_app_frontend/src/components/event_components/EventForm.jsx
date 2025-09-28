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
import { Select, Typography } from '@mui/material';
import AlertSnackbar from '../base_components/AlertSnackbar';
import BackdropSpinner from '../base_components/Backdrop';
import { useCreateEventMutation } from '../../services/eventsAPI';
import { getToken } from '../../services/LocalStorageService';
import { useGetLoggedInUserQuery } from '../../services/userAuthAPI';
import { useDispatch } from 'react-redux';
import { setUserInfo } from '../../features/userSlice';
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import { useForm } from 'react-hook-form'

const schema = yup.object().shape({
    event_name: yup.string().required("Event name is required"),
    subject: yup.string().required("Subject is required"),
    event_department: yup.string().required("Department is required"),
})

export default function EventForm(props) {

    const {
        register, handleSubmit, formState: { errors },
    } = useForm({ resolver: yupResolver(schema) })

    const { access_token } = getToken()

    const { data = [], isSuccess } = useGetLoggedInUserQuery(access_token)

    const [snackAndSpinner, setSnackAndSpinner] = useState({
        openSpinner: true,
        openSnack: true,
        message: "",
        alertType: "success"
    })

    const [eventData, setEventData] = useState({
        user: "",
        event_name: "",
        subject: "",
        event_department: "",
        from_date: "",
        to_date: "",
        event_year: "",
    })

    const [createEvent, responseCreateEvent] = useCreateEventMutation()

    const [from_focus, from_setFocused] = React.useState(false)
    const [from_hasValue, from_setHasValue] = React.useState(false)
    const from_onFocus = () => from_setFocused(true)
    const from_onBlur = () => from_setFocused(false)

    const [to_focus, to_setFocused] = React.useState(false)
    const [to_hasValue, to_setHasValue] = React.useState(false)
    const to_onFocus = () => to_setFocused(true)
    const to_onBlur = () => to_setFocused(false)

    const [dateValidation, setDateValidation] = useState({
        from_date: "",
        to_date: "",
        year: ""
    })

    let maxOffset = 10;
    let thisYear = (new Date()).getFullYear();
    let allYears = [];
    for (let x = 0; x <= maxOffset; x++) {
        allYears.push(thisYear - x)
    }

    const yearList = allYears.map((x) => { return <MenuItem value={x} key={x}>{x}</MenuItem> });

    const dispatch = useDispatch()

    React.useEffect(() => {
        if (data && isSuccess) {
            dispatch(setUserInfo({ email: data.email, name: data.name }))
        }
    }, [data, isSuccess, dispatch])

    React.useEffect(() => {
        if (!props.open) {
            setEventData({ user: "", event_name: "", subject: "", event_department: "", event_year: "", from_date: "", to_date: "" })
        }
    }, [props.open])

    React.useEffect(() => {
        setEventData({ ...eventData, user: data.id })
    }, [data.id])

    function handleEventData(event) {
        const newData = { ...eventData }
        newData[event.target.id] = event.target.value
        setEventData(newData)
    }

    function handleCloseSnackbar() {
        setSnackAndSpinner({ openSnack: false })
    }

    const onSubmit = () => {
        if (eventData.from_date !== "" || eventData.to_date !== "" || eventData.event_year !== "") {
            setEventData({ ...eventData, user: data.id });
            createEvent({ access_token: access_token, eventData: eventData });
            setEventData({ user: "", event_name: "", subject: "", event_department: "", event_year: "", from_date: "", to_date: "" });
            props.onClose()
        }
        else {
            if (eventData.from_date === "" && eventData.to_date === "" && eventData.event_year === "") {
                setDateValidation({ from_date: "From date is required", to_date: "To date is required", year: "Event year is required" })
            }
            else if (eventData.from_date === "") {
                setDateValidation({ ...dateValidation, from_date: "From date is required" })
            }
            else if (eventData.to_date === "") {
                setDateValidation({ ...dateValidation, from_date: "To date is required" })
            }
            else if (eventData.event_year === "") {
                setDateValidation({ ...dateValidation, year: "Event year is required" })
            }
        }
    }

    return (
        <>
            {
                responseCreateEvent.isLoading ?
                    <BackdropSpinner open={snackAndSpinner.openSpinner} /> :
                    <div className='w-full'>
                        <Dialog {...props} >
                            <DialogTitle>Create Event</DialogTitle>
                            <form onSubmit={handleSubmit(onSubmit)} >
                                <DialogContent>
                                    <TextField {...register('event_name')} error={Boolean(errors.event_name)} helperText={errors.event_name?.message} onChange={(e) => handleEventData(e)} value={eventData.event_name} autoFocus margin="dense" id="event_name" label="Event Name" type="text" fullWidth variant="standard" />
                                    <TextField {...register('subject')} error={Boolean(errors.subject)} helperText={errors.subject?.message} onChange={(e) => handleEventData(e)} value={eventData.subject} autoFocus margin="dense" id="subject" label="Event Subject" type="text" fullWidth variant="standard" />
                                    <TextField {...register('event_department')} error={Boolean(errors.event_department)} helpertext={errors.event_department?.message} onChange={(e) => handleEventData(e)} value={eventData.event_department} autoFocus margin="dense" id="event_department" label="Event Department" type="text" fullWidth variant="standard" />
                                    <TextField onFocus={from_onFocus} onBlur={from_onBlur} onChange={(e) => { handleEventData(e); if (e.target.value) from_setHasValue(true); else from_setHasValue(false); }} type={from_hasValue || from_focus ? "date" : "text"} value={eventData.from_date} autoFocus margin="dense" id="from_date" label="Event - From Date" fullWidth variant="standard" />
                                    <Typography fontSize={12} sx={{ color: 'red' }}>{dateValidation.from_date}</Typography>
                                    <TextField onFocus={to_onFocus} onBlur={to_onBlur} onChange={(e) => { handleEventData(e); if (e.target.value) to_setHasValue(true); else to_setHasValue(false); }} type={to_hasValue || to_focus ? 'date' : 'text'} value={eventData.to_date} autoFocus margin="dense" id="to_date" label="Event - To Date" fullWidth variant="standard" />
                                    <Typography fontSize={12} sx={{ color: 'red' }}>{dateValidation.to_date}</Typography>
                                    <FormControl variant="standard" sx={{ width: "100%", marginTop: 1.2 }}  >
                                        <InputLabel id="demo-simple-select-label" variant='standard' >Choose Event Year</InputLabel>
                                        <Select defaultValue='' labelId="demo-simple-select-label" id="event_year" variant="standard" onChange={(e) => setEventData({ ...eventData, event_year: e.target.value })} value={eventData.event_year}>
                                            <MenuItem value="" key="" >
                                                <em>None</em>
                                            </MenuItem>
                                            {yearList}
                                        </Select>
                                    </FormControl>
                                    <Typography fontSize={12} sx={{ color: 'red' }}>{dateValidation.year}</Typography>
                                </DialogContent>
                                <DialogActions>
                                    <Button variant='contained' onClick={props.onClose}>Cancel</Button>
                                    <Button variant='contained' type='submit' >Create</Button>
                                </DialogActions>
                            </form>
                        </Dialog>
                        {
                            responseCreateEvent.data ?
                                <AlertSnackbar open={snackAndSpinner.openSnack} message={responseCreateEvent.data} severity={snackAndSpinner.alertType} onClose={handleCloseSnackbar} autoHideDuration={6000} /> : ""
                        }
                    </div>}
        </>
    );
}