import * as React from "react";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import { useState } from "react";
import AlertSnackbar from "../base_components/AlertSnackbar";
import BackdropSpinner from "../base_components/Backdrop";
import { getToken } from "../../services/LocalStorageService";
import { useGenerateCertificateMutation } from "../../services/certificateGeneratorAPI";
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import { useForm } from 'react-hook-form'
import { getCertificatePath } from "../../services/LocalStorageService";
import { Typography } from "@mui/material";

const schema = yup.object().shape({
    confirm: yup.string().required("Please enter 'YES' if you want to proceed"),
})

export default function GenerateCertificate(props) {

    const {
        register, handleSubmit, formState: { errors },
    } = useForm({ resolver: yupResolver(schema) })

    const [snackAndSpinner, setSnackAndSpinner] = useState({
        openSpinner: true,
        openSnack: true,
        message: "",
        alertType: "success"
    })

    const { access_token } = getToken()

    const { meritCertificate, completionCertificate } = getCertificatePath()

    const [generateCertificate, responseGenerateCertificate] = useGenerateCertificateMutation()

    const [submit, setSubmit] = useState({
        message: "",
        confirm: ""
    })

    React.useEffect(() => {
        if (!props.open) {
            setSubmit({ confirm: "", message: "" })
        }
    }, [props.open])

    const onSubmit = () => {
        if (checkTemplate()) {
            if (submit.confirm.toLowerCase() === 'yes') {
                generateCertificate({ access_token: access_token, merit: meritCertificate, completion: completionCertificate, event_slug: props.event[0]['slug'] })
                setSubmit({ message: "", confirm: "" })
                props.onClose()
            }
        }
        else {
            setSubmit({ message: "Please select a template" })
        }
    }

    const checkTemplate = () => {
        if ((meritCertificate.includes("/certificate-data/merit-certificate-templates/")) || (completionCertificate.includes("/certificate-data/completion-certificate-templates/"))) {
            return true
        }
        else {
            return false
        }
    }

    function handleEventData(event) {
        const newData = { ...submit };
        newData[event.target.id] = event.target.value;
        setSubmit(newData);
    }

    function handleCloseSnackbar() {
        setSnackAndSpinner({ openSnack: false })
    }

    return (
        <>
            {
                responseGenerateCertificate.isLoading ? <BackdropSpinner open={snackAndSpinner.openSpinner} /> :
                    <div className="w-full">
                        <Dialog {...props}>
                            <DialogTitle>
                                Generate Certificate
                                <Typography fontSize={15} marginTop={2}>
                                    Once you click on "Generate" you wouldn't be able to cancel the generation of certificates. Please enter "YES" below to proceed.
                                </Typography>
                                {
                                    <Typography fontSize={13} marginTop={1} sx={{ color: 'red' }}>
                                        {submit.message}
                                    </Typography>
                                }
                            </DialogTitle>
                            <form id="confirm" onSubmit={handleSubmit(onSubmit)} >
                                <DialogContent>
                                    <TextField
                                        {...register('confirm')}
                                        error={Boolean(errors.confirm)}
                                        helperText={errors.confirm?.message}
                                        onChange={(e) => handleEventData(e)}
                                        autoFocus
                                        margin="dense"
                                        id="confirm"
                                        name="confirm"
                                        value={submit.confirm}
                                        label="Ready to generate"
                                        type="text"
                                        fullWidth
                                        variant="standard"
                                    />
                                </DialogContent>
                                <DialogActions>
                                    <Button variant="contained" onClick={props.onClose}>Cancel</Button>
                                    <Button variant="contained" type="submit" >Generate</Button>
                                </DialogActions>
                            </form>
                        </Dialog>
                        {
                            responseGenerateCertificate.data ?
                                <AlertSnackbar
                                    open={snackAndSpinner.openSnack}
                                    message={responseGenerateCertificate.data}
                                    severity={snackAndSpinner.alertType}
                                    onClose={handleCloseSnackbar}
                                    autoHideDuration={6000}
                                /> : ""
                        }
                    </div>
            }
        </>
    );
}
