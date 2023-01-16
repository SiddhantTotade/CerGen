import * as React from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogTitle from '@mui/material/DialogTitle';
import axios from 'axios';
import { useState } from 'react';
import AlertSnackbar from '../base_components/AlertSnackbar';

export default function DeleteParticipant(props) {

    const [openSnack, setOpenSnack] = useState(false)
    const [message, setMessage] = useState("")
    const [alertType, setAlertType] = useState("")

    function handleDelete(id) {

        const url = 'http://127.0.0.1:8000/api/delete-participant/' + id
        axios.delete(url).then(setOpenSnack(true)).then(res => setMessage(res.data)).then(message === "Participant deleted successfully" ? setAlertType("error") : setAlertType("success")).catch(err => console.log(err)).finally(props.onClose).finally(props.onClose)
    }

    function handleCloseSnackbar() {
        setOpenSnack(false)
    }

    return (
        <div className='w-full'>
            <Dialog {...props} >
                <DialogTitle>Delete Participant : {props.participant.event}</DialogTitle>
                <DialogActions>
                    <Button onClick={props.onClose} >Cancel</Button>
                    <Button onClick={() => handleDelete(props.participant.event)} >Yes</Button>
                </DialogActions>
            </Dialog>
            <AlertSnackbar open={openSnack} message={message} severity={alertType} onClose={handleCloseSnackbar} autoHideDuration={6000} />
        </div>
    );
}