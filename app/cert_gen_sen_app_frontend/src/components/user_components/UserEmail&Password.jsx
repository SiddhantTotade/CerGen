import React, { useState } from "react";
import { DialogActions, Button, TextField, Grid, Alert } from "@mui/material";
import { useChangeUserPasswordMutation } from "../../services/userAuthAPI";
import { getToken } from "../../services/LocalStorageService";
import { useNavigate } from "react-router-dom";

export const UserEmailAndPassword = (props) => {

    const { access_token } = getToken()

    const [changeUserPassword] = useChangeUserPasswordMutation()

    const [password, setPassword] = useState({
        new_password: "",
        confirm_new_password: ""
    })

    const navigate = useNavigate()

    const [passwordValidation, setPasswordValidation] = useState("")

    const handlePassword = () => {
        if (password.new_password === password.confirm_new_password) {
            changeUserPassword({ access_token: access_token, password: password });
            props.onClose()
            setTimeout(() => { navigate('/api/login') }, 3000)
        }
        else {
            setPasswordValidation("New Password and Confirm New Password is not matching")
        }
    }

    return (
        <>
            <Grid>
                <TextField margin="dense" disabled defaultValue={props.user.email} id="user_email" label="Email" type="text" fullWidth variant="standard" />
                <TextField onChange={(e) => setPassword({ ...password, new_password: e.target.value })} margin="dense" id="new_password" label="New Password" type="password" fullWidth variant="standard" />
                <TextField onChange={(e) => setPassword({ ...password, confirm_new_password: e.target.value })} margin="dense" id="confirm_new_password" label="Confirm New Password" type="password" fullWidth variant="standard" />
                <DialogActions sx={{ marginTop: "20px" }}>
                    <Button variant="contained" onClick={() => props.onClose()}>Cancel</Button>
                    <Button variant="contained" onClick={() => handlePassword()} >
                        Reset
                    </Button>
                </DialogActions>
                {
                    passwordValidation !== "" ? <Alert severity="error" >{passwordValidation}</Alert> : ""
                }
            </Grid>

        </>
    );
};
