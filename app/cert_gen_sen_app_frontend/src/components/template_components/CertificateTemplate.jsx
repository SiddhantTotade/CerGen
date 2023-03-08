import * as React from "react";
import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogTitle from "@mui/material/DialogTitle";
import axios from "axios";
import { useState, useEffect } from "react";
import AlertSnackbar from "../base_components/AlertSnackbar";
import BackdropSpinner from "../base_components/Backdrop";
import { Box, Tab } from "@mui/material";
import { TabContext, TabList, TabPanel } from "@mui/lab";

export default function CertificateTemplate(props) {
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

  const [value, setValue] = React.useState("1");

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <div>
      <Dialog
        {...props}
        PaperProps={{
          style: {
            minWidth: "50%",
            maxHeight: "90%",
          },
        }}
      >
        <DialogTitle>Template</DialogTitle>
        <Box>
          <TabContext value={value}>
            <Box sx={{ borderBottom: 1, borderColor: "divider" }}>
              <TabList
                onChange={handleChange}
                aria-label="lab API tabs example"
              >
                <Tab label="Choose Template" value="1" />
                <Tab label="Upload Template" value="2" />
              </TabList>
            </Box>
            <TabPanel
              value="1"
              sx={{
                display: "flex",
                gap: "10px",
                width: "100%",
                border: "2px solid green",
              }}
            >
              <div className="border-2 border-red-600 grid grid-cols-2 gap-3 w-2/4">
                <img
                  src="https://images.unsplash.com/photo-1678287759127-1ad7f38855cb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1172&q=80"
                  alt=""
                  width="300px"
                  height="100px"
                />
                <img
                  src="https://images.unsplash.com/photo-1678287759127-1ad7f38855cb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1172&q=80"
                  alt=""
                  width="300px"
                  height="100px"
                />
                <img
                  src="https://images.unsplash.com/photo-1678287759127-1ad7f38855cb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1172&q=80"
                  alt=""
                  width="300px"
                  height="100px"
                />
                <img
                  src="https://images.unsplash.com/photo-1678287759127-1ad7f38855cb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1172&q=80"
                  alt=""
                  width="300px"
                  height="100px"
                />
              </div>
              <div className="border-2 border-red-900 w-2/4"></div>
            </TabPanel>
            <TabPanel value="2">Upload Template</TabPanel>
          </TabContext>
        </Box>
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
