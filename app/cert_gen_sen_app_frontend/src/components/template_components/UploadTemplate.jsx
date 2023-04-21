import React from "react";
import { TextField, Button, DialogActions, Grid, Checkbox, Paper, FormControl, FormControlLabel, Tooltip, Radio, RadioGroup, Typography } from "@mui/material";
import { useState } from "react";
import InfoIcon from "@mui/icons-material/Info";
import { getToken } from "../../services/LocalStorageService";
import { usePreviewTemplateMutation } from "../../services/certificateGeneratorAPI";
import { useUploadCompletionTemplateMutation } from "../../services/certificateGeneratorAPI";
import { useUploadMeritTemplateMutation } from "../../services/certificateGeneratorAPI";
import { CircularProgress } from "@mui/material";
import AlertSnackbar from "../base_components/AlertSnackbar";
import BackdropSpinner from "../base_components/Backdrop";

export const UploadTemplate = (props) => {

  const [snackAndSpinner, setSnackAndSpinner] = useState({
    openSpinner: true,
    openSnack: true,
    message: "",
    alertType: "success"
  })

  const { access_token } = getToken()

  const [previewTemplate, responsePreviewTemplate] = usePreviewTemplateMutation()

  const [uploadCompletionCertificate, responseCompletionCretificate] = useUploadCompletionTemplateMutation()

  const [uploadMeritCertificate, responseMeritCretificate] = useUploadMeritTemplateMutation()

  const [previewFile, setPreviewFile] = React.useState(null);

  const [previewFileValidation, setPreviewFileValidation] = React.useState("");

  const [certificateType, setCertificateType] = useState({
    type: "",
    errorType: ""
  });

  const [contribute, setContribute] = useState(false)

  // const handleUploadTemplate = () => {
  //   let url = "";

  //   if (certificateType === "Participation") {
  //     url = "http://127.0.0.1:8000/api/upload-completion-template/";
  //   } else if (certificateType === "Merit") {
  //     url = "http://127.0.0.1:8000/api/upload-merit-template/";
  //   } else {
  //     return console.log("Select one of the option below");
  //   }

  //   let formData = new FormData();
  //   formData.append("pptx_file", eventFileData);
  //   formData.append("contribute", contribute);

  //   let config = {
  //     headers: {
  //       "content-type": "multipart/form-data",
  //       Authorization: "Token " + localStorage.getItem("token"),
  //     },
  //   };

  //   axios.post(url, formData, config).then((res) => console.log(res));
  // };

  React.useEffect(() => {
    if (!props.props.open) {
      setCertificateType({ type: "", errorType: "" })
    }
  }, [props.props.open])

  const uploadTemplate = () => {
    if (previewFile === null) {
      setPreviewFileValidation("This field is required")
    }
    else {
      if (certificateType.type === "Participation") {
        uploadCompletionCertificate({ access_token: access_token, pptx_file: previewFile, contribute: contribute })
        setCertificateType({ errorType: "", type: "" })
      }
      else if (certificateType.type === "Merit") {
        uploadMeritCertificate({ access_token: access_token, pptx_file: previewFile, contribute: contribute })
        setCertificateType({ errorType: "", type: "" })
      }
      else {
        setCertificateType({ ...certificateType, errorType: "Please select one of the options below" })
      }
    }
  }

  function handleCloseSnackbar() {
    setSnackAndSpinner({ openSnack: false })
  }

  return (
    <>
      {
        responseCompletionCretificate.isLoading || responseMeritCretificate.isLoading ? <BackdropSpinner open={snackAndSpinner.openSpinner} /> : <Grid
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
                    onChange={(e) => setPreviewFile(e.target.files[0])}
                    type='file'
                    autoFocus
                    margin="dense"
                    id="pptx_file"
                    inputProps={{ accept: ".pptx, .ppt" }}
                    label="Upload File"
                    className="upload"
                    fullWidth
                    variant="standard"
                  />
                  <Typography fontSize={13} sx={{ color: 'red' }}>
                    {
                      previewFileValidation
                    }
                  </Typography>
                  <div className="items-center mt-4">
                    <Typography>What you are uploading ?</Typography>
                    <Typography fontSize={13} sx={{ color: 'red' }}>
                      {certificateType.errorType}
                    </Typography>
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
                                  setCertificateType({ ...certificateType, type: "Participation" })
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
                                onChange={(e) => setCertificateType({ ...certificateType, type: "Merit" })}
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
                      control={<Checkbox name="contribute" onClick={() => contribute ? setContribute(false) : setContribute(true)} />}
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
                    "data:image/jpg;base64, " + responsePreviewTemplate.data
                  }
                  alt="Preview"
                />
              </Paper>
            </Grid>
          </Grid>
          <DialogActions sx={{ marginTop: "20px" }}>
            <Button variant="contained">Cancel</Button>
            <Button variant="contained" onClick={() => previewTemplate({ access_token: access_token, previewFile: previewFile })}>
              {responsePreviewTemplate.isLoading ? <CircularProgress size={25} sx={{ color: 'white' }} /> : "Preview"}
            </Button>
            <Button variant="contained" type="submit" onClick={uploadTemplate}>
              Upload
            </Button>
          </DialogActions>
          {
            responseCompletionCretificate.data || responseMeritCretificate.data ?
              <AlertSnackbar
                open={snackAndSpinner.openSnack}
                message={responseCompletionCretificate.data || responseMeritCretificate.data}
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
