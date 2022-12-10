import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';

export default function FileForm(props) {

    return (
        <div className='w-full'>
            <Dialog {...props} >
                <DialogTitle>Add File</DialogTitle>
                <DialogContent>
                    <TextField autoFocus margin="dense" id="event_name" label="File" type="file" fullWidth variant="standard" />
                </DialogContent>
                <DialogActions>
                    <Button onClick={props.onClose}>Cancel</Button>
                    <Button >Create Event</Button>
                </DialogActions>
            </Dialog>
        </div>
    );
}