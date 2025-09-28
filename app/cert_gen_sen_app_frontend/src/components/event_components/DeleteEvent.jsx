import * as React from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogTitle from '@mui/material/DialogTitle';
import { useState } from 'react';
import AlertSnackbar from '../base_components/AlertSnackbar';
import BackdropSpinner from '../base_components/Backdrop';
import { getToken } from '../../services/LocalStorageService';
import { useDeleteEventMutation } from '../../services/eventsAPI';

export default function DeleteEvent(props) {

    const [snackAndSpinner, setSnackAndSpinner] = useState({
        openSpinner: true,
        openSnack: true,
        message: "",
        alertType: "success"
    })

    const { access_token } = getToken()

    const [deleteEvent, responseDeleteEvent] = useDeleteEventMutation()

    function handleCloseSnackbar() {
        setSnackAndSpinner({ openSnack: false })
    }

    return (
        <>
            {
                responseDeleteEvent.isLoading ? <BackdropSpinner open={snackAndSpinner.openSpinner} /> : <div className='w-full'>
                    <Dialog {...props} >
                        <DialogTitle>Delete Event : {props.event.event_name}</DialogTitle>
                        <DialogActions>
                            <Button variant='contained' onClick={props.onClose} >Cancel</Button>
                            <Button variant='contained' onClick={() => { deleteEvent({ access_token: access_token, event_data: props.event }); props.onClose() }} >Yes</Button>
                        </DialogActions>
                    </Dialog>
                    {
                        responseDeleteEvent.data ?
                            <AlertSnackbar open={snackAndSpinner.openSnack} message={responseDeleteEvent.data} severity={snackAndSpinner.alertType} onClose={handleCloseSnackbar} autoHideDuration={6000} /> : ""
                    }
                </div>
            }
        </>
    );
}