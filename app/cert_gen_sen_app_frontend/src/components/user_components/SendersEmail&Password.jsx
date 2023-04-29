import React from "react";
import { DialogActions, Button, TextField, Grid } from "@mui/material";

export const SenderEmailAndPassword = (props) => {

    return (
        <>
            <Grid>
                <TextField margin="dense" id="email" label="Senders Email" type="email" fullWidth variant="standard" />
                <TextField margin="dense" id="sender_password" label="Senders Password" type="password" fullWidth variant="standard" />
                <TextField margin="dense" id="phone" label="Senders Phone" type="tel" fullWidth variant="standard" />
                <DialogActions sx={{ marginTop: "20px" }}>
                    <Button variant="contained" onClick={() => props.onClose()}>Cancel</Button>
                    <Button variant="contained" >
                        Set Credentials
                    </Button>
                </DialogActions>
            </Grid>
        </>
    );
};
