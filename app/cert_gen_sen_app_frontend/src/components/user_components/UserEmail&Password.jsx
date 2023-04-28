import React from "react";
import { DialogActions, Button, TextField, Grid } from "@mui/material";

export const UserEmailAndPassword = (props) => {

    return (
        <>
            <Grid>
                <TextField margin="dense" disabled defaultValue={props.user.email} id="user_email" label="Email" type="text" fullWidth variant="standard" />
                <TextField margin="dense" id="new_password" label="New Password" type="text" fullWidth variant="standard" />
                <TextField margin="dense" id="confirm_new_password" label="Confirm New Password" type="text" fullWidth variant="standard" />
                <DialogActions sx={{ marginTop: "20px" }}>
                    <Button variant="contained">Cancel</Button>
                    <Button variant="contained" >
                        Reset
                    </Button>
                </DialogActions>
            </Grid>
        </>
    );
};
