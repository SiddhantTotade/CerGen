import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';

export default function EventForm(props) {

    return (
        <div className='w-full'>
            <Dialog {...props} >
                <DialogTitle>Add Event</DialogTitle>
                <DialogContent>
                    <TextField autoFocus margin="dense" id="name" label="Event Name" type="email" fullWidth variant="standard" />
                    <TextField autoFocus margin="dense" id="name"  type="date" fullWidth variant="standard" />
                    <TextField autoFocus margin="dense" id="name" label="Email Address" type="email" fullWidth variant="standard" />
                </DialogContent>
                <DialogActions>
                    <Button onClick={props.onClose}>Cancel</Button>
                </DialogActions>
            </Dialog>
        </div>
    );
}