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
import { useCreateParticipantMutation } from "../../services/participantsAPI";
import { useSpecificEventDetailQuery } from "../../services/eventsAPI";
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import { useForm } from 'react-hook-form'
import { CircularProgress } from "@mui/material";
import { Box } from "@mui/system";

const schema = yup.object().shape({
  participant_name: yup.string().required("Name is required"),
  participant_id: yup.string().required("Id is required"),
  email: yup.string().email("Invalid email").required("Email is required"),
  phone: yup.number().required("Phone is required"),
  certificate_status: yup.string().required("Certificate status is required ")
})

export default function CreateParticipant(props) {

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

  const [participantData, setParticipantData] = useState({
    event: "",
    participant_name: "",
    participant_id: "",
    email: "",
    phone: "",
    certificate_status: "",
  });

  const [createParticipant, responseCreateParticipant] = useCreateParticipantMutation()

  const { data = [], isLoading } = useSpecificEventDetailQuery({ access_token: access_token, event_slug: props.event_slug.toLowerCase() })

  React.useEffect(() => {
    if (!props.open) {
      setParticipantData({ event: "", participant_name: "", participant_id: "", email: "", phone: "", certificate_status: "" })
    }
  }, [props.open])
  
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

    return certificateId.replace(/-/g, "");
  }

  const onSubmit = () => {
    createParticipant({ access_token: access_token, participant_data: participantData, event: data[0].id, phone: handlePhone(), certificate_id: generateCertificateId(participantData.participant_id, data[0].event_name, data[0].event_department, data[0].from_date) })
    setParticipantData({ event: "", student_name: "", student_id: "", email: "", phone: "", certificate_status: "", certificate_id: "" })
    props.onClose()
  }

  function handleEventData(event) {
    const newData = { ...participantData };
    newData[event.target.id] = event.target.value;
    setParticipantData(newData);
  }

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
        responseCreateParticipant.isLoading ? <BackdropSpinner open={snackAndSpinner.openSpinner} /> :
          <div className="w-full">
            <Dialog {...props}>
              <DialogTitle sx={{ display: 'flex', justifyContent: 'space-between' }}>
                Add Participant
                <Box>
                  {
                    isLoading ? <CircularProgress size={25} /> : ""
                  }
                </Box>
              </DialogTitle>
              <form onSubmit={handleSubmit(onSubmit)} >
                <DialogContent>
                  <TextField
                    {...register('participant_name')}
                    error={Boolean(errors.participant_name)}
                    helperText={errors.participant_name?.message}
                    onChange={(e) => handleEventData(e)}
                    value={participantData.participant_name}
                    autoFocus
                    margin="dense"
                    id="participant_name"
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
                    value={participantData.participant_id}
                    autoFocus
                    margin="dense"
                    id="participant_id"
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
                    value={participantData.email}
                    autoFocus
                    margin="dense"
                    id="email"
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
                    value={participantData.phone}
                    autoFocus
                    margin="dense"
                    id="phone"
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
                    value={participantData.certificate_status}
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
                  <Button variant="contained" onClick={props.onClose}>Cancel</Button>
                  <Button variant="contained" type="submit" >Create</Button>
                </DialogActions>
              </form>
            </Dialog>
            {
              responseCreateParticipant.data ?
                <AlertSnackbar
                  open={snackAndSpinner.openSnack}
                  message={responseCreateParticipant.data}
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
