import * as React from "react";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import { useState } from "react";
import AlertSnackbar from "../base_components/AlertSnackbar";
import BackdropSpinner from "../base_components/Backdrop";
import { getToken } from "../../services/LocalStorageService";
import { useUpdateParticipantMutation } from "../../services/participantsAPI";
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import { useForm } from 'react-hook-form'

const schema = yup.object().shape({
  participant_name: yup.string().required("Name is required"),
  participant_id: yup.string().required("Id is required"),
  email: yup.string().email("Invalid email").required("Email is required"),
  phone: yup.number().required("Phone is required"),
  certificate_status: yup.string().required("Certificate status is required ")
})

export default function UpdateParticipant(props) {

  const {
    register, handleSubmit, formState: { errors },
  } = useForm({ resolver: yupResolver(schema) })

  const [snackAndSpinner, setSnackAndSpinner] = useState({
    openSpinner: true,
    openSnack: true,
    message: "",
    alertType: "success"
  })

  const { access_token } = getToken()

  const [updateParticipant, responseUpdateParticipant] = useUpdateParticipantMutation()

  // const [participantData, setParticipantData] = useState({
  //   event: props.participant.event,
  //   participant_name: props.participant.participant_name,
  //   participant_id: props.participant.participant_id,
  //   email: props.participant.email,
  //   phone: props.participant.phone,
  //   certificate_status: props.participant.certificate_status,
  //   certificate_id: props.participant.certificate_id,
  // });

  const [participantData, setParticipantData] = useState(props.participant)

  // const [updateParticipantData, setUpdateParticipantData] = useState({
  //   event: "",
  //   student_name: "",
  //   student_id: "",
  //   email: "",
  //   phone: "",
  //   certificate_status: "",
  //   certificate_id: "",
  // });

  React.useEffect(() => {
    if (!props.open) {
      setParticipantData({ event: "", participant_name: "", participant_id: "", email: "", phone: "", certificate_status: "" })
    }
  }, [props.open])


  // useEffect(() => {
  //   const event_url = window.location.href;
  //   const new_event_url = event_url
  //     .replace("3000", "8000")
  //     .replace("event", "event-details");
  //   axios
  //     .get(new_event_url, {
  //       headers: { Authorization: "Token " + localStorage.getItem("token") },
  //     })
  //     .then((res) => setEventsData(res.data));
  // }, []);

  // useEffect(() => {
  // settingParticipantData();
  // eslint-disable-next-line
  // }, []);

  // function handleSubmit(e) {
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
  // }
  function generateCertificateId(
    participant_id,
    event_name,
    event_department,
    event_date
  ) {
    let event_name_char = event_name.match(/\b(\w)/g).join("");
    let random_num = Math.floor(1000 + Math.random() * 9000);
    let certificateId =
      participant_id + event_name_char + event_department + event_date + random_num;

    return certificateId;
  }

  const onSubmit = () => {
    console.log(participantData);
    // updateParticipant({ access_token: access_token, participant_data: participantData, phone: handlePhone(), certificate_id: generateCertificateId(participantData.participant_id, props.event_detail.event_name, props.event_detail.event_department, props.event_detail.from_date) })
    // setParticipantData({ event: "", student_name: "", student_id: "", email: "", phone: "", certificate_status: "", certificate_id: "" })
    // props.onClose()
  }

  const handleEventData = (event) => {
    const { name, value } = event.target
    setParticipantData((prevValues) => ({ ...prevValues, [name]: value }))
    // const newData = { ...updateParticipantData };
    // newData[event.target.id] = event.target.value;
    // setUpdateParticipantData(newData);
  }

  // function settingParticipantData() {
  //   setParticipantData(props.participant);
  // }

  function handlePhone() {
    let phone = participantData.phone.includes("+91") ? participantData.phone : "+91" + participantData.phone
    return phone
  }

  function handleCloseSnackbar() {
    setSnackAndSpinner({ openSnack: false })
  }


  return (
    <>
      {
        responseUpdateParticipant.isLoading ? <BackdropSpinner open={snackAndSpinner.openSpinner} /> :
          <div className="w-full">
            <Dialog {...props}>
              <DialogTitle>Edit Participant</DialogTitle>
              <form onSubmit={handleSubmit(onSubmit)}>
                <DialogContent>
                  <TextField
                    {...register('participant_name')}
                    error={Boolean(errors.participant_name)}
                    helperText={errors.participant_name?.message}
                    onChange={(e) => handleEventData(e)}
                    // defaultValue={participantData.participant_name}
                    value={props.participant.participant_name}
e                    autoFocus
                    margin="dense"
                    id="participant_name"
                    name="participant_name"
                    label="Participant Name"
                    type="text"
                    fullWidth
                    variant="standard"
                  />
                  <TextField
                    {...register('participant_id')}
                    error={Boolean(errors.participant_id)}
                    helperText={errors.participant_id?.message}
                    onChange={(e) => handleEventData(e)}
                    defaultValue={participantData.participant_id}
                    autoFocus
                    margin="dense"
                    id="participant_id"
                    name="participant_id"
                    label="Participant Id"
                    type="text"
                    fullWidth
                    variant="standard"
                  />
                  <TextField
                    {...register('email')}
                    error={Boolean(errors.email)}
                    helperText={errors.email?.message}
                    onChange={(e) => handleEventData(e)}
                    defaultValue={participantData.email}
                    autoFocus
                    margin="dense"
                    id="email"
                    name="email"
                    label="Participant Email"
                    type="email"
                    fullWidth
                    variant="standard"
                  />
                  <TextField
                    {...register('phone', { max: 13, min: 10, maxLength: 13 })}
                    error={Boolean(errors.phone)}
                    helperText={errors.phone?.message}
                    onChange={(e) => handleEventData(e)}
                    defaultValue={participantData.phone}
                    autoFocus
                    margin="dense"
                    id="phone"
                    name="phone"
                    label="Participant Phone"
                    type="phone"
                    fullWidth
                    variant="standard"
                  />
                  <TextField
                    {...register('certificate_status')}
                    error={Boolean(errors.certificate_status)}
                    helperText={errors.certificate_status?.message}
                    onChange={(e) => handleEventData(e)}
                    defaultValue={participantData.certificate_status}
                    autoFocus
                    margin="dense"
                    id="certificate_status"
                    name="certificate_status"
                    label="Certificate Status"
                    type="text"
                    fullWidth
                    variant="standard"
                  />
                </DialogContent>
                <DialogActions>
                  <Button variant="contained" onClick={props.onClose} >Cancel</Button>
                  <Button variant="contained" type="submit" >Update</Button>
                </DialogActions>
              </form>
            </Dialog>
            {
              responseUpdateParticipant.data ?

                <AlertSnackbar
                  open={snackAndSpinner.openSnack}
                  message={responseUpdateParticipant.data}
                  severity={snackAndSpinner.alertType}
                  onClose={handleCloseSnackbar}
                  autoHideDuration={6000}
                /> : ""
            }
          </div>
      }
    </>
  );
}
