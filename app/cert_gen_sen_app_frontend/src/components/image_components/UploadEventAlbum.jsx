import React, { useEffect } from "react";
import {
    TextField,
    Button,
    DialogActions,
    Grid,
    Paper,
    FormControl,
} from "@mui/material";
import 'react-responsive-carousel/lib/styles/carousel.min.css'
import { Carousel } from 'react-responsive-carousel'
import { useState } from "react";
import axios from "axios";

export const UploadEventAlbum = (props) => {
    const [previewFile, setPreviewFile] = useState(null);

    let fileObj = []
    let fileArray = []

    // useEffect(() => {
    //     if (!selectedFile) {
    //         setPreviewFile(undefined)
    //         return
    //     }

    //     const objectUrl = URL.createObjectURL(selectedFile)
    //     setPreviewFile(objectUrl)

    //     return () => URL.revokeObjectURL(objectUrl)
    // }, [selectedFile])

    const onSelectFile = (e) => {
        // if (!e.target.files || e.target.files.length === 0) {
        //     setSelectedFile(undefined)
        // }

        fileObj.push(e.target.files)
        for (let i = 0; i < fileObj[0].length; i++) {
            fileArray.push(URL.createObjectURL(fileObj[0][i]))
        }

        setPreviewFile(fileArray)
    }

    const convertBase64 = (selectedFile) => {
        return new Promise((resolve, reject) => {
            let reader = new FileReader()
            reader.readAsDataURL(selectedFile)
            reader.onload = () => {
                resolve(reader.result)
            }
            reader.onerror = (error) => {
                reject(error)
            }
        })
    }

    // const handleUploadTemplate = async () => {
    //     const base64Image = await convertBase64(selectedFile)

    //     const url = 'http://127.0.0.1:8000/api/upload-event-album/' + props.participant.event

    //     let formData = new FormData();
    //     formData.append('participant_image', base64Image)

    //     let config = {
    //         headers: {
    //             "content-type": "multipart/form-data",
    //             Authorization: "Token " + localStorage.getItem("token"),
    //         },
    //     };

    //     axios.patch(url, formData, config).then((res) => console.log(res));
    // };

    return (
        <>
            <Grid
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
                            <Carousel className="w-full" swipeable={false} showArrows={true} showThumbs={false} dynamicHeight={true} showIndicators={false} showStatus={false} interval={2000} transitionTime={500} autoPlay={true} infiniteLoop={true} emulateTouch={true} stopOnHover={true} >
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
                    {/* <Button variant="contained" onClick={handleUploadTemplate}>
                        Upload
                    </Button> */}
                </DialogActions>
            </Grid>
        </>
    );
};
