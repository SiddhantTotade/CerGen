import React, { useEffect } from "react";
import { TextField, Button, DialogActions, Grid, Paper } from "@mui/material";
import { useState } from "react";
import axios from "axios";
import { UseScript } from "../base_components/UseScript.jsx";
import $ from "jquery";
import "jquery-ui-dist/jquery-ui";
import Jquery from "../../external_libraries/PPTXjs/js/jquery-1.11.3.min.js";
import PPT_1 from "../../external_libraries/PPTXjs/js/ppt_1.js";
// import "../../external_libraries/PPTX2HTML/css/font-awesome.min.css";
// import "../../external_libraries/PPTX2HTML/css/pptx2html.css";
// import "../../external_libraries/PPTXjs/js/jquery-1.11.3.min.js";
// import "../../external_libraries/PPTXjs/js/jszip.min.js"
// import "../../external_libraries/PPTXjs/js/filereader.js"
// import "../../external_libraries/PPTXjs/js/d3.min.js"
// import "../../external_libraries/PPTXjs/js/nv.d3.min.js"
// import "../../external_libraries/PPTXjs/js/pptxjs.js"
// import "../../external_libraries/PPTXjs/js/divs2slides.js"
// import "../../external_libraries/PPTXjs/js/jquery.fullscreen-min.js"
// import "../../external_libraries/PPTXjs/js/ppt_1.js";

const MyComponent = (props) => {
  UseScript(Jquery);
  // UseScript("../../external_libraries/PPTXjs/js/jszip.min.js");
  // UseScript("../../external_libraries/PPTXjs/js/filereader.js");
  // UseScript("../../external_libraries/PPTXjs/js/d3.min.js");
  // UseScript("../../external_libraries/PPTXjs/js/nv.d3.min.js");
  // UseScript("../../external_libraries/PPTXjs/js/pptxjs.js");
  // UseScript("../../external_libraries/PPTXjs/js/divs2slides.js");
  // UseScript("../../external_libraries/PPTXjs/js/jquery.fullscreen-min.js");
  UseScript(PPT_1);
  // UseScript("../../external_libraries/PPTXjs/js/ppt_2.js");
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

  useEffect(() => {
    console.log(PPT_1);
  });

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
