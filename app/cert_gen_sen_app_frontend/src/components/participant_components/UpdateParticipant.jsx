import * as React from "react";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import axios from "axios";
import { useState, useEffect } from "react";
import AlertSnackbar from "../base_components/AlertSnackbar";
import BackdropSpinner from "../base_components/Backdrop";
import { getToken } from "../../services/LocalStorageService";

export default function UpdateParticipant(props) {
  const [snackAndSpinner, setSnackAndSpinner] = useState({
    openSpinner: true,
    openSnack: true,
    message: "",
    alertType: "success"
  })

  let [eventsData, setEventsData] = useState([]);

  Object.values(eventsData).map((event) => {
    return (eventsData = event.id);
  });

  const [participantData, setParticipantData] = useState({
    event: "",
    student_name: "",
    student_id: "",
    email: "",
    phone: "",
    certificate_status: "",
    certificate_id: "",
  });

  const [updateParticipantData, setUpdateParticipantData] = useState({
    event: "",
    student_name: "",
    student_id: "",
    email: "",
    phone: "",
    certificate_status: "",
    certificate_id: "",
  });

  useEffect(() => {
    const event_url = window.location.href;
    const new_event_url = event_url
      .replace("3000", "8000")
      .replace("event", "event-details");
    axios
      .get(new_event_url, {
        headers: { Authorization: "Token " + localStorage.getItem("token") },
      })
      .then((res) => setEventsData(res.data));
  }, []);

  useEffect(() => {
    settingParticipantData();
    // eslint-disable-next-line
  }, []);

  function handleSubmit(e) {
    // e.preventDefault();
    // const certificateId = generateCertificateId(
    //   updateParticipantData.student_id === ""
    //     ? participantData.student_id
    //     : updateParticipantData.student_id,
    //   props.event_slug,
    //   props.event_detail.eventDepartment,
    //   props.event_detail.eventDate
    // );
    // setOpenSpinner(true);
    // setTimeout(() => {
    //   setOpenSpinner(false);
    // }, 2000);
    // const url =
    //   "http://127.0.0.1:8000/api/update-participant/" + props.participant.event;
    // axios
    //   .put(
    //     url,
    //     {
    //       event: eventsData,
    //       student_name:
    //         updateParticipantData.student_name === ""
    //           ? participantData.student_name
    //           : updateParticipantData.student_name,
    //       student_id:
    //         updateParticipantData.student_id === ""
    //           ? participantData.student_id
    //           : updateParticipantData.student_id,
    //       email:
    //         updateParticipantData.email === ""
    //           ? participantData.email
    //           : updateParticipantData.email,
    //       phone:
    //         updateParticipantData.phone === ""
    //           ? participantData.phone
    //           : updateParticipantData.phone,
    //       certificate_status:
    //         updateParticipantData.certificate_status === ""
    //           ? participantData.certificate_status
    //           : updateParticipantData.certificate_status,
    //       certificate_id: certificateId,
    //     },
    //     { headers: { Authorization: "Token " + localStorage.getItem("token") } }
    //   )
    //   .then(
    //     setTimeout(() => {
    //       setOpenSnack(true);
    //     }, 2000)
    //   )
    //   .then((res) => setMessage(res.data))
    //   .then(
    //     message === "Participant updated successfully"
    //       ? setAlertType("error")
    //       : setAlertType("success")
    //   )
    //   .catch((err) => console.log(err))
    //   .finally(props.onClose);
  }

  function handleEventData(event) {
    const newData = { ...updateParticipantData };
    newData[event.target.id] = event.target.value;
    setUpdateParticipantData(newData);
  }

  function settingParticipantData() {
    setParticipantData(props.participant);
  }

  function handleCloseSnackbar() {
    // setOpenSnack(false);
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

    setUpdateParticipantData({ certificate_id: certificateId });

    return certificateId;
  }

  return (
    <div className="w-full">
      <Dialog {...props}>
        <DialogTitle>Edit Participant</DialogTitle>
        <DialogContent>
          <TextField
            sx={{ display: "none" }}
            disabled
            defaultValue={props.participant.event}
            autoFocus
            margin="dense"
            id="event"
            label="Participant Id"
            type="text"
            fullWidth
            variant="standard"
          />
          <TextField
            onChange={(e) => handleEventData(e)}
            defaultValue={props.participant.student_name}
            autoFocus
            margin="dense"
            id="student_name"
            label="Participant Name"
            type="text"
            fullWidth
            variant="standard"
          />
          <TextField
            onChange={(e) => handleEventData(e)}
            defaultValue={props.participant.student_id}
            autoFocus
            margin="dense"
            id="student_id"
            label="Participant Id"
            type="text"
            fullWidth
            variant="standard"
          />
          <TextField
            onChange={(e) => handleEventData(e)}
            defaultValue={props.participant.email}
            autoFocus
            margin="dense"
            id="email"
            label="Participant Email"
            type="email"
            fullWidth
            variant="standard"
          />
          <TextField
            onChange={(e) => handleEventData(e)}
            defaultValue={props.participant.phone}
            autoFocus
            margin="dense"
            id="phone"
            label="Participant Phone"
            type="phone"
            fullWidth
            variant="standard"
          />
          <TextField
            onChange={(e) => handleEventData(e)}
            defaultValue={props.participant.certificate_status}
            autoFocus
            margin="dense"
            id="certificate_status"
            label="Certificate Status"
            type="text"
            fullWidth
            variant="standard"
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={props.onClose}>Cancel</Button>
          <Button onClick={handleSubmit}>Update Participant</Button>
        </DialogActions>
      </Dialog>
      {/* <BackdropSpinner open={openSpinner} />
      <AlertSnackbar
        open={openSnack}
        message={message}
        severity={alertType}
        onClose={handleCloseSnackbar}
        autoHideDuration={6000}
      /> */}
    </div>
  );
}
