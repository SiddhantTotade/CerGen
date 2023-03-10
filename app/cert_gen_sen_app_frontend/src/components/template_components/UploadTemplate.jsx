import React from "react";
import { TextField, Button, DialogActions, Grid, Paper } from "@mui/material";
import { useState } from "react";
import axios from "axios";

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
    // console.log(config);
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
                autoFocus
                margin="dense"
                id="upload_file"
                label="Upload File"
                type="file"
                fullWidth
                variant="standard"
                onChange={uploadFile}
              />
            </Grid>
          </Grid>
          <Grid item xs={6}>
            <Paper
              elevation={12}
              style={{
                width: "100%",
                height: "100%",
                // background: selectedImage
                //   ? `url(${selectedImage}) no-repeat center center / cover`
                //   : "white",
              }}
            ></Paper>
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
