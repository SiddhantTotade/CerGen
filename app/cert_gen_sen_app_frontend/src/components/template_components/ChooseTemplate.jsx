import React, { useState } from "react";
import { DialogActions, Button, Paper, Grid } from "@mui/material";
import { useEffect } from "react";
import axios from "axios";

export const ChooseTemplate = () => {
  const [selectedImage, setSelectedImage] = useState(null);

  const [images, setImages] = useState("");

  useEffect(() => {
    const url = "http://127.0.0.1:8000/api/upload-completion-template/";

    axios
      .get(url, {
        headers: { Authorization: "Token " + localStorage.getItem("token") },
      })
      .then((res) => setImages(res.data));
  }, []);

  return (
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
            {Object.values(images).map((imageUrl, index) => (
              <Grid item key={index}>
                <Paper
                  onClick={() => setSelectedImage(imageUrl.template_img)}
                  style={{
                    width: 100,
                    height: 100,
                    background: `url(${
                      "http://127.0.0.1:8000" + imageUrl.template_img
                    }) no-repeat center center / cover`,
                    cursor: "pointer",
                  }}
                />
              </Grid>
            ))}
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
            <img
              src={
                selectedImage ? "http://127.0.0.1:8000/" + selectedImage : ""
              }
            />
          </Paper>
        </Grid>
      </Grid>
      <DialogActions sx={{ marginTop: "20px" }}>
        <Button variant="contained">Cancel</Button>
        <Button variant="contained">Use this template</Button>
      </DialogActions>
    </Grid>
  );
};
