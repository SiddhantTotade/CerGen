import React, { useEffect } from "react";
import {
    TextField,
    Button,
    DialogActions,
    Grid,
    Paper,
    FormControl,
} from "@mui/material";
import { useState } from "react";
import axios from "axios";

export const UploadParticipantImage = (props) => {
    const [previewFile, setPreviewFile] = useState();
    const [selectedFile, setSelectedFile] = useState();

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

    const handleUploadTemplate = () => {
        const url = ""

        let formData = new FormData();

        let config = {
            headers: {
                "content-type": "multipart/form-data",
                Authorization: "Token " + localStorage.getItem("token"),
            },
        };

        axios.post(url, formData, config).then((res) => console.log(res));
    };

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
                                    inputProps={{ accept: "application/vnd.ms-powerpoint" }}
                                    label="Upload File"
                                    className="upload"
                                    fullWidth
                                    variant="standard"
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
            </Grid>
        </>
    );
};
