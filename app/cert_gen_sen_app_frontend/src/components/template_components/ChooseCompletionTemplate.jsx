import React, { useState } from "react";
import { DialogActions, Button, Paper, Grid, Typography } from "@mui/material";
import { setCertificatePath } from "../../services/LocalStorageService";
import { getToken } from "../../services/LocalStorageService";
import { useGetCompletionCertificateQuery } from "../../services/certificateGeneratorAPI";
import { useGetContributeCompletionCertificateQuery } from "../../services/certificateGeneratorAPI";
import AlertBar from "../base_components/AlertBar";
import LoaderSkeleton from "../base_components/LoaderSkeleton";

export const ChooseCompletionTemplate = () => {

  const [selectedImage, setSelectedImage] = useState({
    url: null,
    id: "",
  });
  const { access_token } = getToken()

  const [alert, setAlert] = useState(false)

  const { data = [], isLoading } = useGetCompletionCertificateQuery(access_token)

  const contributedCertificates = useGetContributeCompletionCertificateQuery(access_token)

  console.log(data === "Failed to get images" ? contributedCertificates.data : data.concat(contributedCertificates.data === undefined ? contributedCertificates.data : []));

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
              {
                isLoading ? <LoaderSkeleton barPadding={10} /> : (data === "Failed to get images" && contributedCertificates.data === undefined) ?
                  (
                    <Typography>No Template Found</Typography>
                  ) :
                  (data === "Failed to get images" ? contributedCertificates.data : data.concat(contributedCertificates.data === undefined ? contributedCertificates.data : [])).map((imageUrl, index) => (
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
              }
            </Grid>
          </Grid>
          <Grid item xs={6} sx={{ display: 'grid', gap: '10px' }}>
            <Paper
              elevation={12}
              style={{
                width: "100%",
                height: "100%",
                display: "grid",
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
          {
            alert ?
              <AlertBar message="Done" barWidth={100} /> : ""
          }
        </Grid>
        <DialogActions sx={{ marginTop: "20px" }}>
          <Button variant="contained">Cancel</Button>
          <Button
            variant="contained"
            onClick={() => { setAlert(true); setTimeout(() => { setAlert(false) }, 2000) }}
          >
            Use this template
          </Button>
        </DialogActions>
      </Grid>
    </>
  );
};
