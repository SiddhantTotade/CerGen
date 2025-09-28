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

export default function DeleteParticipant(props) {

    const [snackAndSpinner, setSnackAndSpinner] = useState({
        openSpinner: true,
        openSnack: true,
        message: "",
        alertType: "success"
    })

    const { access_token } = getToken()

    const [deleteParticipant, responseDeleteParticipant] = useDeleteParticipantMutation()

    function handleCloseSnackbar() {
        setSnackAndSpinner({ openSnack: false })
    }

    return (
        <>
            {
                responseDeleteParticipant.isLoading ? <BackdropSpinner open={snackAndSpinner.openSpinner} /> : <div className='w-full'>
                    <Dialog {...props} >
                        <DialogTitle>Delete Participant : {props.participant.participant_name}</DialogTitle>
                        <DialogActions>
                            <Button variant='contained' onClick={props.onClose} >Cancel</Button>
                            <Button variant='contained' onClick={() => { deleteParticipant({ access_token: access_token, participant_data: props.participant }); props.onClose() }} >Yes</Button>
                        </DialogActions>
                    </Dialog>
                    {
                        responseDeleteParticipant.data ?
                            <AlertSnackbar open={snackAndSpinner.openSnack} message={responseDeleteParticipant.data} severity={snackAndSpinner.alertType} onClose={handleCloseSnackbar} autoHideDuration={6000} /> : ""
                    }
                </div>
            }
        </>
    );
}