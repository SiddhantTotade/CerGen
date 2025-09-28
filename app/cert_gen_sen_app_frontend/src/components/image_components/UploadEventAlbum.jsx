import React from "react";
import {
    TextField,
    Button,
    DialogActions,
    Grid,
    Paper,
    FormControl,
    Typography,
} from "@mui/material";
import 'react-responsive-carousel/lib/styles/carousel.min.css'
import { Carousel } from 'react-responsive-carousel'
import { useState } from "react";
import { useUploadAlbumImagesMutation } from '../../services/participantsImagesAPI';
import { getToken } from "../../services/LocalStorageService";
import BackdropSpinner from "../base_components/Backdrop";
import AlertSnackbar from "../base_components/AlertSnackbar";

export const UploadEventAlbum = (props) => {

    const [snackAndSpinner, setSnackAndSpinner] = useState({
        openSpinner: true,
        openSnack: true,
        message: "",
        alertType: "success"
    })

    const { access_token } = getToken()

    const [eventAlbum, responesImageAlbum] = useUploadAlbumImagesMutation()

    const [previewFile, setPreviewFile] = useState(null);

    const [imageValidation, setImageValidation] = useState(false)

    let fileObj = []
    let fileArray = []
    const [images, setImages] = useState([])

    const onSelectFile = (e) => {
        if (!e.target.files || e.target.files.length === 0) {
            setPreviewFile(undefined)
        }

        fileObj.push(e.target.files)
        for (let i = 0; i < fileObj[0].length; i++) {
            fileArray.push(URL.createObjectURL(fileObj[0][i]))
        }

        setPreviewFile(fileArray)
        setImages([...images, ...e.target.files])
    }

    const handleUploadTemplate = async () => {
        if (images.length === 0) {
            setImageValidation(true)
            setTimeout(() => {
                setImageValidation(false)
            }, 2000)
        }
        else {
            eventAlbum({ access_token: access_token, album: images, event_slug: props.event_slug })
        }
    };

    function handleCloseSnackbar() {
        setSnackAndSpinner({ openSnack: false })
    }

    return (
        <>
            {
                responesImageAlbum.isLoading ? <BackdropSpinner open={snackAndSpinner.openSpinner} /> : <Grid
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
                                        label="Upload File"
                                        className="upload"
                                        fullWidth
                                        variant="standard"
                                        inputProps={{
                                            multiple: true,
                                            accept: "image/*"
                                        }}
                                    />
                                    {
                                        imageValidation ? <Typography fontSize={13} sx={{ color: 'red' }}>This field if required</Typography> : ""
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
                                <Carousel className="w-full" swipeable={true} showArrows={true} showThumbs={false} dynamicHeight={true} showIndicators={false} showStatus={false} emulateTouch={true} stopOnHover={true} >
                                    {(previewFile || []).map((url, id) => (
                                        <div key={id}>
                                            <img
                                                src={url}
                                                alt="Preview"
                                                className="h-96 object-contain"
                                            />
                                        </div>
                                    ))}
                                </Carousel>
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
                        responesImageAlbum.data ?
                            <AlertSnackbar
                                open={snackAndSpinner.openSnack}
                                message={responesImageAlbum.data}
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
