import React, { useState } from "react";
import { DialogActions, Button, Paper, Grid, Typography } from "@mui/material";
import { setCertificatePath } from "../../services/LocalStorageService";
import { getToken } from "../../services/LocalStorageService";
import { useGetCompletionCertificateQuery } from "../../services/certificateGeneratorAPI";
import { useGetContributeCompletionCertificateQuery } from "../../services/certificateGeneratorAPI";

export const ChooseCompletionTemplate = () => {

  const [selectedImage, setSelectedImage] = useState({
    url: null,
    id: "",
  });

  const { access_token } = getToken()

  const { data = [], isLoading } = useGetCompletionCertificateQuery(access_token)

  const contributedCertificates = useGetContributeCompletionCertificateQuery(access_token)

  const completionAndContributed = data.concat(contributedCertificates)

  // const [images, setImages] = useState("");

  // const [contributeImage, setContributeImages] = useState("")

  // console.log(responseCompletionCertificate);

  // console.log(contributedCompletionCertificate);

  // useEffect(() => {
  //   const url = "http://127.0.0.1:8000/api/upload-completion-template/";

  //   axios
  //     .get(url, {
  //       headers: { Authorization: "Token " + localStorage.getItem("token") },
  //     })
  //     .then((res) => setImages(res.data));
  // }, []);

  // useEffect(() => {
  //   const url = "http://127.0.0.1:8000/api/contribute-completion-template/";

  //   axios
  //     .get(url, {
  //       headers: { Authorization: "Token " + localStorage.getItem("token") },
  //     })
  //     .then((res) => setContributeImages(res.data));
  // }, []);

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
          <Grid item xs={4} height={350} sx={{ overflow: "auto" }}>
            <Grid container spacing={2}>
              {(data !== "Failed to get images" || contributedCertificates !== "Failed to get images") ? (
                (data !== "Failed to get images" ? data.concat(contributedCertificates) : contributedCertificates).map((imageUrl, index) => (
                  <Grid item key={index}>
                    <Paper
                      onClick={() =>
                        setSelectedImage({
                          url: imageUrl.template_img,
                          id: index,
                        })
                      }
                      style={{
                        width: 150,
                        height: 100,
                        background: `url(${"http://127.0.0.1:8000" + imageUrl.template_img
                          }) no-repeat center center / cover`,
                        cursor: "pointer",
                        border:
                          selectedImage.id === index ? "2px solid blue" : "2px solid gainsboro",
                      }}
                    />
                  </Grid>
                ))
              ) : (
                <Typography>No template</Typography>
              )}
            </Grid>
          </Grid>
          <Grid item xs={6}>
            <Paper
              elevation={12}
              style={{
                width: "100%",
                height: "100%",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
              }}
            >
              <img
                src={
                  selectedImage.url
                    ? "http://127.0.0.1:8000/" + selectedImage.url
                    : ""
                }
                alt="Preview"
              />
            </Paper>
          </Grid>
        </Grid>
        <DialogActions sx={{ marginTop: "20px" }}>
          <Button variant="contained">Cancel</Button>
          <Button
            variant="contained"
            onClick={setCertificatePath(selectedImage.url)}
          >
            Use this template
          </Button>
        </DialogActions>
      </Grid>
    </>
  );
};
