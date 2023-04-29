import React, { useState } from "react";
import { DialogActions, Button, TextField, Grid } from "@mui/material";
import { useChangeUserPasswordMutation } from "../../services/userAuthAPI";
import { getToken } from "../../services/LocalStorageService";

export const UserEmailAndPassword = (props) => {

    const { access_token } = getToken()

    const [changeUserPassword, responceChangeUserPassword] = useChangeUserPasswordMutation()

    const [password, setPassword] = useState({
        new_password: "",
        confirm_new_pasword: ""
    })

    const handlePassword = () => {
    }

    console.log(password);

    return (
        <>
            <Grid>
                <TextField margin="dense" disabled defaultValue={props.user.email} id="user_email" label="Email" type="text" fullWidth variant="standard" />
                <TextField onChange={(e) => setPassword({ ...password, new_password: e.target.value })} margin="dense" id="new_password" label="New Password" type="text" fullWidth variant="standard" />
                <TextField onChange={(e) => setPassword({ ...password, confirm_new_pasword: e.target.value })} margin="dense" id="confirm_new_password" label="Confirm New Password" type="text" fullWidth variant="standard" />
                <DialogActions sx={{ marginTop: "20px" }}>
                    <Button variant="contained">Cancel</Button>
                    <Button variant="contained" onClick={() => changeUserPassword({ access_token: access_token, password: password })} >
                        Reset
                    </Button>
                </DialogActions>
            </Grid>
        </>
    );
};
