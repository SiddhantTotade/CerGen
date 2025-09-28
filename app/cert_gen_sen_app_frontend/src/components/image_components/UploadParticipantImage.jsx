import React, { useEffect } from "react";
import { TextField, Button, DialogActions, Grid, Paper, FormControl, Typography } from "@mui/material";
import { useState } from "react";
import { useUploadParticipantImageMutation } from "../../services/participantsImagesAPI";
import { getToken } from "../../services/LocalStorageService";
import BackdropSpinner from "../base_components/Backdrop";
import AlertSnackbar from "../base_components/AlertSnackbar";

export const UploadParticipantImage = (props) => {

    const [snackAndSpinner, setSnackAndSpinner] = useState({
        openSpinner: true,
        openSnack: true,
        message: "",
        alertType: "success"
    })

    const { access_token } = getToken()

    const [uploadParticipantImage, responseParticipantImage] = useUploadParticipantImageMutation()

    const [previewFile, setPreviewFile] = useState(null);

    const [selectedFile, setSelectedFile] = useState(null);

    const [imageValidation, setImageValidation] = useState(false)

    useEffect(() => {
        if (!selectedFile) {
            setPreviewFile(undefined)
            return
        }

        const objectUrl = URL.createObjectURL(selectedFile)
        setPreviewFile(objectUrl)

        return () => URL.revokeObjectURL(objectUrl)
    }, [selectedFile])

    const onSelectFile = (e) => {
        if (!e.target.files || e.target.files.length === 0) {
            setSelectedFile(undefined)
        }

        setSelectedFile(e.target.files[0])
    }

    const handleUploadTemplate = async () => {
        if (selectedFile === null) {
            setImageValidation(true)
            setTimeout(() => {
                setImageValidation(false)
            }, 2000)
        }
        else {
            uploadParticipantImage({ access_token: access_token, imgSrc: selectedFile, id: props.participant.id })
        }
    };

    function handleCloseSnackbar() {
        setSnackAndSpinner({ openSnack: false })
    }

    return (
        <>
            {
                responseParticipantImage.isLoading ? <BackdropSpinner open={snackAndSpinner.openSpinner} /> : <Grid
                    sx={{
                        marginTop: "20px",
                        display: "flex",
                        justifyContent: "center",
                        flexDirection: "column",
                    }}
                >
                    <Grid
                        container
                        spacing={2}
                        sx={{ display: "flex", justifyContent: 'space-between' }}
                    >
                        <Grid
                            item
                            xs={4}
                            height={290}
                            width={900}
                            sx={{ overflow: "auto", display: "flex" }}
                        >
                            <Grid
                                container
                                spacing={1}
                                sx={{ display: "flex", alignItems: "center" }}
                            >
                                <FormControl>
                                    <TextField
                                        onChange={onSelectFile}
                                        type="file"
                                        autoFocus
                                        margin="dense"
                                        id="upload_file"
                                        inputProps={{ accept: "application/vnd.ms-powerpoint" }}
                                        label="Upload File"
                                        className="upload"
                                        fullWidth
                                        variant="standard"
                                    />
                                    {
                                        imageValidation ? <Typography fontSize={13} sx={{ color: 'red' }}>This field is required</Typography> : ""
                                    }
                                </FormControl>
                            </Grid>
                        </Grid>
                        <Grid item xs={6}>
                            <Paper
                                elevation={12}
                                style={{
                                    width: "100%",
                                    height: "100%",
                                    display: 'flex',
                                    justifyContent: 'center',
                                    alignItems: 'center'
                                }}
                            >
                                {selectedFile &&
                                    <img
                                        src={previewFile}
                                        alt="Preview"
                                        width={230}
                                    />
                                }
                            </Paper>
                        </Grid>
                    </Grid>
                    <DialogActions sx={{ marginTop: "20px" }}>
                        <Button variant="contained" onClick={props.onClose}>Cancel</Button>
                        <Button variant="contained" onClick={handleUploadTemplate}>
                            Upload
                        </Button>
                    </DialogActions>
                    {
                        responseParticipantImage.data ?
                            <AlertSnackbar
                                open={snackAndSpinner.openSnack}
                                message={responseParticipantImage.data}
                                severity={snackAndSpinner.alertType}
                                onClose={handleCloseSnackbar}
                                autoHideDuration={6000}
                            /> : ""
                    }
                </Grid>
            }
        </>
    );
};
