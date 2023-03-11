import React from "react";
import { TextField, Button, DialogActions, Grid, Paper } from "@mui/material";
import { useState } from "react";
import axios from "axios";
import Cookie from "js-cookie";

export const UploadTemplate = () => {
  const [file_focus, file_setFocused] = React.useState(false);
  const [file_hasValue, file_setHasValue] = React.useState(false);
  const file_onFocus = () => file_setFocused(true);
  const file_onBlur = () => file_setFocused(false);

  const [eventFileData, setEventFileData] = React.useState({
    pptx_file: null,
  });

  const [file, setFile] = useState(null);

  axios.defaults.xsrfCookieName = "csrftoken";
  axios.defaults.xsrfHeaderName = "X-CSRFToken";

  function handleFileChange(event) {
    setEventFileData(event.target.files[0]);
    uploadFile()
  }

  const uploadFile = (e) => {
    // setFile(URL.createObjectURL(e.target.files[0]));

    const formData = new FormData();
    formData.append("pptx_file", eventFileData);

    const url = "http://127.0.0.1:8000/api/ppttohtml/";
    const config = {
      headers: {
        "content-type": "multipart/form-data",
        Authorization: "Token " + localStorage.getItem("token"),
        "X-CSRFToken": Cookie.get("csrftoken"),
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
          sx={{ display: "flex", justifyContent: "center", gap: "100px" }}
        >
          <Grid
            item
            xs={4}
            height={350}
            sx={{ overflow: "auto", display: "flex" }}
          >
            <Grid
              container
              spacing={2}
              sx={{ display: "flex", alignItems: "center" }}
            >
              <TextField
                onFocus={file_onFocus}
                onBlur={file_onBlur}
                onChange={(e) => {
                  handleFileChange(e);
                  if (e.target.value) file_setHasValue(true);
                  else file_setHasValue(false);
                }}
                type={file_hasValue || file_focus ? "file" : "file"}
                autoFocus
                margin="dense"
                id="upload_file"
                label="Upload File"
                className="upload"
                fullWidth
                variant="standard"
              />
            </Grid>
          </Grid>
          <Grid item xs={6}>
            <Paper
              elevation={12}
              style={{
                width: "100%",
                height: "100%",
              }}
            >
              <div id="result"></div>
            </Paper>
          </Grid>
        </Grid>

        <DialogActions sx={{ marginTop: "20px" }}>
          <Button variant="contained">Cancel</Button>
          <Button variant="contained">Upload</Button>
        </DialogActions>
      </Grid>
    </>
  );
};
