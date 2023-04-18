import * as React from "react";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";
import axios from "axios";
import { useState, useEffect } from "react";
import AlertSnackbar from "../base_components/AlertSnackbar";
import BackdropSpinner from "../base_components/Backdrop";
import { Box, Tab } from "@mui/material";
import PropTypes from "prop-types";
import { Tabs } from "@mui/material";
import { UploadTemplate } from "./UploadTemplate";
import { ChooseCompletionTemplate } from "./ChooseCompletionTemplate";
import { ChooseMeritTemplate } from "./ChooseMeritCertificate";

function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 2 }}>
          <div>{children}</div>
        </Box>
      )}
    </div>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.number.isRequired,
  value: PropTypes.number.isRequired,
};

function a11yProps(index) {
  return {
    id: `simple-tab-${index}`,
    "aria-controls": `simple-tabpanel-${index}`,
  };
}

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

  const [value, setValue] = React.useState(0);

  const [eventsData, setEventsData] = useState([]);
  const event_url = window.location.href;

  eventsData.map((event) => {
    return (participantData.event = event.id);
  });

  // useEffect(() => {
  //   const new_event_url = event_url
  //     .replace("3000", "8000")
  //     .replace("event", "event-details");

  //   const fetchData = async () => {
  //     try {
  //       const response = await axios.get(new_event_url);
  //       setEventsData(response.data);
  //     } catch (error) {
  //       console.log(error);
  //     }
  //   };
  //   fetchData();
  // }, [event_url]);

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

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <div>
      <Dialog
        {...props}
        PaperProps={{
          style: {
            minWidth: "60%",
          },
        }}
      >
        <DialogTitle>Templates</DialogTitle>
        <Box sx={{ width: "100%" }}>
          <Box sx={{ borderBottom: 1, borderColor: "divider" }}>
            <Tabs
              value={value}
              onChange={handleChange}
              aria-label="basic tabs example"
            >
              <Tab label="Choose Participantion Template" {...a11yProps(0)} />
              <Tab label="Choose Merit Template" {...a11yProps(1)} />
              <Tab label="Upload Template" {...a11yProps(2)} />
            </Tabs>
          </Box>
          <TabPanel value={value} index={0}>
            <ChooseCompletionTemplate />
          </TabPanel>
          <TabPanel value={value} index={1}>
            <ChooseMeritTemplate />
          </TabPanel>
          <TabPanel value={value} index={2}>
            <UploadTemplate />
          </TabPanel>
        </Box>
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
