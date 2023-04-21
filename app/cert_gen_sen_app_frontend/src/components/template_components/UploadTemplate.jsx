import React from "react";
import { TextField, Button, DialogActions, Grid, Checkbox, Paper, FormControl, FormControlLabel, Tooltip, Radio, RadioGroup, Typography } from "@mui/material";
import { useState } from "react";
import InfoIcon from "@mui/icons-material/Info";
import { getToken } from "../../services/LocalStorageService";
import { usePreviewTemplateMutation } from "../../services/certificateGeneratorAPI";
import { useUploadCompletionTemplateMutation } from "../../services/certificateGeneratorAPI";
import { useUploadMeritTemplateMutation } from "../../services/certificateGeneratorAPI";
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import { useForm } from 'react-hook-form'

const schema = yup.object().shape({
  pptx_file: yup.object().required("File is required"),
})

export const UploadTemplate = () => {

  const {
    register, handleSubmit, formState: { errors },
  } = useForm({ resolver: yupResolver(schema) })

  const { access_token } = getToken()

  const [previewTemplate, responsePreviewTemplate] = usePreviewTemplateMutation()

  const [uploadCompletionCertificate, responseCompletionCretificate] = useUploadCompletionTemplateMutation()

  const [uploadMeritCertificate, responseMeritCretificate] = useUploadMeritTemplateMutation()

  const [previewFile, setPreviewFile] = React.useState(null);

  console.log(responsePreviewTemplate);

  const [certificateType, setCertificateType] = useState("");
  const [contribute, setContribute] = useState(false)

  // const [previewData, setPreviewData] = useState(null);
  // localStorage.setItem("certificatePreview", previewFile);

  function handleFileChange(event) {
    setPreviewFile(event.target.files[0]);
  }

  // const previewTemplateFile = () => {
  //   let formData = new FormData();
  //   formData.append("pptx_file", eventFileData);

  //   const url = "http://127.0.0.1:8000/api/preview-certificate/";

  //   let config = {
  //     headers: {
  //       "content-type": "multipart/form-data",
  //       Authorization: "Token " + localStorage.getItem("token"),
  //     },
  //   };

  //   axios.post(url, formData, config).then((res) => setPreviewFile(res.data));
  // };

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

  const onSubmit = () => {
    // createParticipant({ access_token: access_token, participant_data: participantData, event: data[0].id, phone: handlePhone(), certificate_id: generateCertificateId(participantData.participant_id, data[0].event_name, data[0].event_department, data[0].from_date) })
    // setParticipantData({ event: "", student_name: "", student_id: "", email: "", phone: "", certificate_status: "", certificate_id: "" })
    // props.onClose()
  }

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
        {/* <form onSubmit={handleSubmit(onSubmit)}> */}
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
                    {...register('pptx_file')}
                    error={Boolean(errors.pptx_file)}
                    helperText={errors.pptx_file?.message}
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
              Preview
            </Button>
            <Button variant="contained" type="submit">
              Upload
            </Button>
          </DialogActions>
        {/* </form> */}
      </Grid>
    </>
  );
};
