import React, { useState } from "react";
import { DialogActions, Button, Paper, Grid, Typography } from "@mui/material";
import { getToken } from "../../services/LocalStorageService";
import { useGetMeritCertificateQuery } from "../../services/certificateGeneratorAPI";
import { useGetContributeMeritCertificateQuery } from "../../services/certificateGeneratorAPI";

export const ChooseMeritTemplate = () => {

  const { access_token } = getToken()

  const [selectedImage, setSelectedImage] = useState({
    url: null,
    id: "",
  });

  const { data = [], isLoading } = useGetMeritCertificateQuery(access_token)

  const contributedCertificates = useGetContributeMeritCertificateQuery(access_token)

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
              {(data === "Failed to get images" || data.length === 0 || contributedCertificates === undefined) ?
                (
                  <Typography>No template</Typography>
                ) : (
                  (data.length !== 0 ? data.concat(contributedCertificates.data) : contributedCertificates.data).map((imageUrl, index) => (
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
            onClick={localStorage.setItem(
              "MeritCertificatePath",
              selectedImage.url
            )}
          >
            Use this template
          </Button>
        </DialogActions>
      </Grid>
    </>
  );
};
