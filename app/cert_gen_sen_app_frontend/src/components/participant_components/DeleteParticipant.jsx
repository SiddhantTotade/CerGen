import * as React from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogTitle from '@mui/material/DialogTitle';
import axios from 'axios';
import { useState } from 'react';

export default function DeleteParticipant(props) {

    let [eventsData, setEventsData] = useState([])

    const handleDelete = async (id) => {

        const url = 'http://127.0.0.1:8000/api/delete-participant/' + id

        const deleteData = async () => {

            try {
                const response = await axios.delete(url).finally(props.onClose)
                setEventsData(response.data)
            }
            catch (error) {
                console.log(error);
            }
        }
        deleteData()
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
        </div>
    );
}