import * as React from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogTitle from '@mui/material/DialogTitle';
import { useState } from 'react';
import AlertSnackbar from '../base_components/AlertSnackbar';
import BackdropSpinner from '../base_components/Backdrop';
import { getToken } from '../../services/LocalStorageService';
import { useDeleteParticipantMutation } from '../../services/participantsAPI';
// import AlertSnackbar from '../base_components/AlertSnackbar';
// import BackdropSpinner from '../base_components/Backdrop';

export default function DeleteParticipant(props) {

    const [openSnack, setOpenSnack] = useState(false)
    const [message, setMessage] = useState("")
    const [alertType, setAlertType] = useState("")
    const [openSpinner, setOpenSpinner] = useState(false)

    const { access_token } = getToken()

    const [deleteParticipant, responseDeleteParticipant] = useDeleteParticipantMutation()

    function handleDelete(id) {
        // setOpenSpinner(true)
        // setTimeout(() => { setOpenSpinner(false) }, 1000)
        // const url = 'http://127.0.0.1:8000/api/delete-participant/' + id
        // axios.delete(url, { headers: { "Authorization": "Token " + localStorage.getItem("token") } }).then(setTimeout(() => { setOpenSnack(true) }, 1000)).then(res => setMessage(res.data)).then(message === "Participant deleted successfully" ? setAlertType("error") : setAlertType("success")).catch(err => console.log(err)).finally(props.onClose).finally(props.onClose)
    }

    function handleCloseSnackbar() {
        setOpenSnack(false)
    }

    return (
        <div className='w-full'>
            <Dialog {...props} >
                <DialogTitle>Delete Participant : {props.participant.participant_name}</DialogTitle>
                <DialogActions>
                    <Button variant='contained' onClick={props.onClose} >Cancel</Button>
                    <Button variant='contained' onClick={() => { deleteParticipant({ access_token: access_token, participant_data: props.participant }); props.onClose() }} >Yes</Button>
                </DialogActions>
            </Dialog>
            <BackdropSpinner open={openSpinner} />
            <AlertSnackbar open={openSnack} message={message} severity={alertType} onClose={handleCloseSnackbar} autoHideDuration={6000} />
        </div>
    );
}