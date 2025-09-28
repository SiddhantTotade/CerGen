import React, { useState } from "react";
import { DialogActions, Button, TextField, Grid } from "@mui/material";
import { useSenderCredentialMutation } from "../../services/userAuthAPI";
import { getToken } from "../../services/LocalStorageService";
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import { useForm } from 'react-hook-form'
import BackdropSpinner from "../base_components/Backdrop";
import AlertSnackbar from "../base_components/AlertSnackbar";

const schema = yup.object().shape({
    email: yup.string().email("Invalid email").required("Email is required"),
    password: yup.string().required("Password is required"),
    phone: yup.number().required("Phone is required"),
})

export const SenderEmailAndPassword = (props) => {

    const [snackAndSpinner, setSnackAndSpinner] = useState({
        openSpinner: true,
        openSnack: true,
        message: "",
        alertType: "success"
    })

    const {
        register, handleSubmit, formState: { errors },
    } = useForm({ resolver: yupResolver(schema) })

    const { access_token } = getToken()

    const [senderCredential, responseCredential] = useSenderCredentialMutation()

    const [credential, setCredential] = useState({
        email: null,
        password: null,
        phone: null
    })

    const handleCredential = () => {
        senderCredential({ access_token: access_token, credential: credential, phone: handlePhone() })
        props.onClose()
    }

    function handlePhone() {
        let phone = credential.phone.includes("+91") ? credential.phone : "+91" + credential.phone
        return phone
    }

    function handleCloseSnackbar() {
        setSnackAndSpinner({ openSnack: false })
    }

    return (
        <>
            {
                responseCredential.isLoading ? <BackdropSpinner open={snackAndSpinner.openSpinner} /> :
                    <div>
                        <Grid>
                            <form onSubmit={handleSubmit(handleCredential)}>
                                <TextField
                                    {...register('email')} error={Boolean(errors.email)} helperText={errors.email?.message} name="email" onChange={(e) => setCredential({ ...credential, email: e.target.value })} margin="dense" id="email" label="Senders Email" type="email" fullWidth variant="standard" />
                                <TextField {...register('password')} error={Boolean(errors.password)} helperText={errors.password?.message} name="password" onChange={(e) => setCredential({ ...credential, password: e.target.value })} margin="dense" id="sender_password" label="Senders Password" type="password" fullWidth variant="standard" />
                                <TextField {...register('phone')} error={Boolean(errors.phone)} helperText={errors.phone?.message} name="phone" onChange={(e) => setCredential({ ...credential, phone: e.target.value })} margin="dense" id="phone" label="Senders Phone" type="tel" fullWidth variant="standard" />
                                <DialogActions sx={{ marginTop: "20px" }}>
                                    <Button variant="contained" onClick={() => props.onClose()}>Cancel</Button>
                                    <Button variant="contained" type="submit" >
                                        Set Credentials
                                    </Button>
                                </DialogActions>
                            </form>
                        </Grid>
                        {
                            responseCredential.data ?
                                <AlertSnackbar open={snackAndSpinner.openSnack} message={responseCredential.data} severity={snackAndSpinner.alertType} onClose={handleCloseSnackbar} autoHideDuration={6000} /> : ""
                        }
                    </div>
            }
        </>
    );
};
