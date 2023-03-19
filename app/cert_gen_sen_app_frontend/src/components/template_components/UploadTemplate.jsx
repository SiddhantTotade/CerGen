import React from "react";
import {
  TextField,
  Button,
  DialogActions,
  Grid,
  Checkbox,
  Paper,
  FormControl,
  FormControlLabel,
  Tooltip,
  Radio,
  RadioGroup,
  Typography,
} from "@mui/material";
import { useState } from "react";
import axios from "axios";
import InfoIcon from "@mui/icons-material/Info";

export const UploadTemplate = () => {
  const [file_focus, file_setFocused] = React.useState(false);
  const [file_hasValue, file_setHasValue] = React.useState(false);
  const file_onFocus = () => file_setFocused(true);
  const file_onBlur = () => file_setFocused(false);

  const [eventFileData, setEventFileData] = React.useState({
    pptx_file: "",
  });

  const [certificateType, setCertificateType] = useState("");

  const [previewFile, setPreviewFile] = useState(null);
  localStorage.setItem("certificatePreview", previewFile);

  function handleFileChange(event) {
    setEventFileData(event.target.files[0]);
  }

  const previewTemplateFile = () => {
    let formData = new FormData();
    formData.append("pptx_file", eventFileData);

    const url = "http://127.0.0.1:8000/api/preview-certificate/";

    let config = {
      headers: {
        "content-type": "multipart/form-data",
        Authorization: "Token " + localStorage.getItem("token"),
      },
    };

    axios.post(url, formData, config).then((res) => setPreviewFile(res.data));
  };

  const handleUploadTemplate = () => {
    let url = "";

    if (certificateType === "Participation") {
      url = "http://127.0.0.1:8000/api/upload-completion-template/";
    } else if (certificateType === "Merit") {
      url = "http://127.0.0.1:8000/api/upload-merit-template/";
    } else {
      return console.log("Select one of the option below");
    }

    let formData = new FormData();
    formData.append("pptx_file", eventFileData);

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
              spacing={1}
              sx={{ display: "flex", alignItems: "center" }}
            >
              <FormControl>
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
                  inputProps={{ accept: "application/vnd.ms-powerpoint" }}
                  label="Upload File"
                  className="upload"
                  fullWidth
                  variant="standard"
                />
                <div className="items-center mt-4">
                  <Typography>What you are uploading ?</Typography>
                  <div className="flex">
                    <FormControl>
                      <RadioGroup
                        aria-labelledby="demo-radio-buttons-group-label"
                        defaultValue=""
                        name="radio-buttons-group"
                      >
                        <FormControlLabel
                          sx={{
                            display: "flex",
                            alignItems: "center",
                            justifyContent: "flex-start",
                          }}
                          control={
                            <Radio
                              onChange={(e) =>
                                setCertificateType("Participation")
                              }
                            />
                          }
                          label="Participation Template"
                          value="Participation"
                        />
                        <FormControlLabel
                          sx={{
                            display: "flex",
                            alignItems: "center",
                            justifyContent: "flex-start",
                          }}
                          control={
                            <Radio
                              onChange={(e) => setCertificateType("Merit")}
                            />
                          }
                          label="Merit Template"
                          value="Merit"
                        />
                      </RadioGroup>
                    </FormControl>
                  </div>
                </div>
                <div className="flex items-center mt-4">
                  <FormControlLabel
                    sx={{
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "flex-start",
                    }}
                    control={<Checkbox name="contribute" />}
                    label="Contribute"
                  />
                  <Tooltip
                    sx={{ cursor: "pointer" }}
                    title="By checking this other people can also use your template/s"
                  >
                    <InfoIcon
                      sx={{ cursor: "pointer", color: "#8cd0fa", width: "6%" }}
                    />
                  </Tooltip>
                </div>
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
              <img
                src={
                  "data:image/jpg;base64, " +
                  localStorage.getItem("certificatePreview")
                }
                alt="Preview"
              />
            </Paper>
          </Grid>
        </Grid>
        <DialogActions sx={{ marginTop: "20px" }}>
          <Button variant="contained">Cancel</Button>
          <Button variant="contained" onClick={previewTemplateFile}>
            Preview
          </Button>
          <Button variant="contained" onClick={handleUploadTemplate}>
            Upload
          </Button>
        </DialogActions>
      </Grid>
    </>
  );
};
