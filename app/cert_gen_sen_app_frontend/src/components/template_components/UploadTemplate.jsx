import * as React from "react";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import { Card, CardActions, CardContent, Typography } from "@mui/material";
import axios from "axios";
import { useState, useEffect } from "react";
import AlertSnackbar from "../base_components/AlertSnackbar";
import BackdropSpinner from "../base_components/Backdrop";
import { Box, Tab } from "@mui/material";
import { TabContext, TabList, TabPanel } from "@mui/lab";

export default function UploadTemplate(props) {
  const [openSnack, setOpenSnack] = useState(false);
  const [message, setMessage] = useState("");
  const [alertType, setAlertType] = useState("");
  const [openSpinner, setOpenSpinner] = useState(false);

  const [participantData, setParticipantData] = useState({
    event: "",
    student_name: "",
    student_id: "",
    email: "",
    certificate_status: "",
  });

  const [eventsData, setEventsData] = useState([]);
  const event_url = window.location.href;

  eventsData.map((event) => {
    return (participantData.event = event.id);
  });

  useEffect(() => {
    const new_event_url = event_url
      .replace("3000", "8000")
      .replace("event", "event-details");

    const fetchData = async () => {
      try {
        const response = await axios.get(new_event_url);
        setEventsData(response.data);
      } catch (error) {
        console.log(error);
      }
    };
    fetchData();
  }, [event_url]);

  function handleSubmit(e) {
    e.preventDefault();
    const certificateId = generateCertificateId(
      participantData.student_id,
      props.event_slug,
      props.event_detail.eventDepartment,
      props.event_detail.eventDate
    );
    setOpenSpinner(true);
    setTimeout(() => {
      setOpenSpinner(false);
    }, 5000);
    const url = "http://127.0.0.1:8000/api/create-participant/";
    axios
      .post(
        url,
        {
          event: participantData.event,
          student_name: participantData.student_name,
          student_id: participantData.student_id,
          email: participantData.email,
          certificate_status: participantData.certificate_status,
          certificate_id: certificateId,
        },
        { headers: { Authorization: "Token " + localStorage.getItem("token") } }
      )
      .then(
        setTimeout(() => {
          setOpenSnack(true);
        }, 5000)
      )
      .then((res) => setMessage(res.data))
      .then(
        message === "Participant added successfully"
          ? setAlertType("error")
          : setAlertType("success")
      )
      .catch((err) => console.log(err))
      .finally(props.onClose);
  }

  function handleEventData(event) {
    const newData = { ...participantData };
    newData[event.target.id] = event.target.value;
    setParticipantData(newData);
  }

  function handleCloseSnackbar() {
    setOpenSnack(false);
  }

  function generateCertificateId(
    student_id,
    event_name,
    event_department,
    event_date
  ) {
    let event_name_char = event_name.match(/\b(\w)/g).join("");
    let random_num = Math.floor(1000 + Math.random() * 9000);
    let certificateId =
      student_id + event_name_char + event_department + event_date + random_num;

    return certificateId;
  }

  return (
    <div className="w-full">
      <Dialog {...props} sx={{ maxWidth: "100%", width: "100%" }}>
        <DialogTitle>Template</DialogTitle>
        <div className="flex justify-center items-center">
          <DialogContent>
            <Card sx={{ minWidth: 10 }}>
              <CardContent>
                <Typography
                  sx={{ fontSize: 14 }}
                  color="text.secondary"
                  gutterBottom
                >
                  Word of the Day
                </Typography>
                <Typography sx={{ mb: 1.5 }} color="text.secondary">
                  adjective
                </Typography>
                <Typography variant="body2">
                  well meaning and kindly.
                  <br />
                  {'"a benevolent smile"'}
                </Typography>
              </CardContent>
              <CardActions>
                <Button size="small">Learn More</Button>
              </CardActions>
            </Card>
          </DialogContent>
          <DialogContent>
            <TextField
              //   onChange={(e) => handleEventData(e)}
              autoFocus
              margin="dense"
              id="upload_file"
              label="Upload File"
              type="file"
              fullWidth
              inputProps={{ accept: "application/ppt, application/pptx" }}
              variant="standard"
            />
          </DialogContent>
        </div>
        <DialogActions>
          <Button onClick={props.onClose}>Cancel</Button>
          <Button onClick={handleSubmit}>Create Participant</Button>
        </DialogActions>
      </Dialog>
      <BackdropSpinner open={openSpinner} />
      <AlertSnackbar
        open={openSnack}
        message={message}
        severity={alertType}
        onClose={handleCloseSnackbar}
        autoHideDuration={6000}
      />
    </div>
  );
}
