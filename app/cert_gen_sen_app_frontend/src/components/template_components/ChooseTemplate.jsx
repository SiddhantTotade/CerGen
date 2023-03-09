import React, { useState } from "react";
import { DialogActions, Button, Paper, Grid } from "@mui/material";

export const ChooseTemplate = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const images = [
    "https://images.unsplash.com/photo-1678329887232-a48991da8286?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
    "https://plus.unsplash.com/premium_photo-1674740444237-6677634b6838?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyNXx8fGVufDB8fHx8&auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1678347761208-b181d59781b1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw4fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1678329887232-a48991da8286?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
    "https://plus.unsplash.com/premium_photo-1674740444237-6677634b6838?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyNXx8fGVufDB8fHx8&auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1678347761208-b181d59781b1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw4fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1678329887232-a48991da8286?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
    "https://plus.unsplash.com/premium_photo-1674740444237-6677634b6838?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyNXx8fGVufDB8fHx8&auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1678347761208-b181d59781b1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw4fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
  ];
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
            {images.map((imageUrl, index) => (
              <Grid item key={index}>
                <Paper
                  onClick={() => setSelectedImage(imageUrl)}
                  style={{
                    width: 100,
                    height: 100,
                    background: `url(${imageUrl}) no-repeat center center / cover`,
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
              background: selectedImage
                ? `url(${selectedImage}) no-repeat center center / cover`
                : "white",
            }}
          />
        </Grid>
      </Grid>
      <DialogActions sx={{ marginTop: "20px" }}>
        <Button variant="contained">Cancel</Button>
        <Button variant="contained">Use this template</Button>
      </DialogActions>
    </Grid>
  );
};
