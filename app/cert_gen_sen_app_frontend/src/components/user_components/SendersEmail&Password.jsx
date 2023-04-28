import React from "react";
import { DialogActions, Button, TextField, Grid } from "@mui/material";

export const SenderEmailAndPassword = () => {

    return (
        <>
            <Grid>
                <TextField margin="dense" id="new_password" label="Senders Email" type="text" fullWidth variant="standard" />
                <TextField margin="dense" id="confirm_new_password" label="Senders Password" type="text" fullWidth variant="standard" />
                <DialogActions sx={{ marginTop: "20px" }}>
                    <Button variant="contained">Cancel</Button>
                    <Button variant="contained" >
                        Set Email & Password
                    </Button>
                </DialogActions>
            </Grid>
        </>
    );
};
