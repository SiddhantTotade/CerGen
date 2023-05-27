import React, { useState } from "react";
import { DialogActions, Button, Paper, Grid, Typography } from "@mui/material";
import { getToken } from "../../services/LocalStorageService";
import { useGetMeritCertificateQuery } from "../../services/certificateGeneratorAPI";
import { useGetContributeMeritCertificateQuery } from "../../services/certificateGeneratorAPI";
import { setMeritPath } from "../../services/LocalStorageService";
import AlertBar from "../base_components/AlertBar";
import LoaderSkeleton from "../base_components/LoaderSkeleton";

const card = 4

const templateCard = [...Array(card)].map((e, i) =>
  <LoaderSkeleton barPadding={9.1} barWidth="40%" key={i} />
)

export const ChooseMeritTemplate = (props) => {

  const { access_token } = getToken()

  const [selectedImage, setSelectedImage] = useState({
    url: null,
    id: "",
  });

  const [alert, setAlert] = useState(false)

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
            <Grid container spacing={2} sx={{ gap: '10px' }}>
              {
                isLoading ? templateCard : ((data === "Failed to get images" || data.length === 0) && (contributedCertificates.data === "Failed to get images" || contributedCertificates.data === undefined)) ?
                  (
                    <Typography>No Template Found</Typography>

                  ) :
                  (contributedCertificates.data === undefined || contributedCertificates.data === "Failed to get images" ? data : data === "Failed to get images" || data.length === 0 ? contributedCertificates.data : data.concat(contributedCertificates.data)).map((imageUrl, index) => (
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
            {
              alert ?
                <AlertBar message="Done" barWidth='100%' /> : ""
            }
          </Grid>
        </Grid>
        <DialogActions sx={{ marginTop: "20px" }}>
          <Button variant="contained" onClick={props.props.onClose} >Cancel</Button>
          <Button
            variant="contained"
            onClick={() => { setAlert(true); setMeritPath({ merit: selectedImage.url }); setTimeout(() => { setAlert(false) }, 2000) }}
          >
            Use this template
          </Button>
        </DialogActions>
      </Grid>
    </>
  );
};
