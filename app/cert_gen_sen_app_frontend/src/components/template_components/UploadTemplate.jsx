import React, { useEffect } from "react";
import { TextField, Button, DialogActions, Grid, Paper } from "@mui/material";
import { useState } from "react";
import axios from "axios";
import { UseScript } from "../base_components/UseScript.jsx";
import "jquery-ui-dist/jquery-ui";

const MyComponent = (props) => {
  UseScript("https://github.com/g21589/PPTX2HTML/blob/12f654fd23008f4b57c6ae43c5144eb370115b6f/js/jquery-1.11.3.min.js")
};

export const UploadTemplate = () => {
  const [file, setFile] = useState(null);

  const uploadFile = (e) => {
    // setFile(URL.createObjectURL(e.target.files[0]));

    const formData = new FormData();
    formData.append("ppt_file", e.target.files[0]);

    const url = "http://127.0.0.1:8000/api/ppt-to-html/";
    const config = {
      headers: {
        "content-type": "multipart/form-data",
        Authorization: "Token " + localStorage.getItem("token"),
      },
    };

    axios.post(url, formData, config).then((res) => console.log(res));
  };

  useEffect(() => {});

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
              <MyComponent />
              <TextField
                autoFocus
                margin="dense"
                id="uploadFileInput"
                label="Upload File"
                inputProps={{
                  accept:
                    "application/vnd.openxmlformats-officedocument.presentationml.presentation",
                }}
                type="file"
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
