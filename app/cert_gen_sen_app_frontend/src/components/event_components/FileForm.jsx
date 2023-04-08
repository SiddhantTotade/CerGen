import * as React from "react";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogTitle from "@mui/material/DialogTitle";
import Select from "@mui/material/Select";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import { useState } from "react";
import BackdropSpinner from "../base_components/Backdrop";
import AlertSnackbar from "../base_components/AlertSnackbar";
import { useUploadParticipantsMutation } from "../../services/participantsAPI";
import { useGetAllEventsQuery } from "../../services/eventsAPI";
import { getToken } from "../../services/LocalStorageService";
import LoaderSkeleton from "../base_components/LoaderSkeleton";

export default function FileForm(props) {
  
  const [snackAndSpinner, setSnackAndSpinner] = useState({
    openSpinner: true,
    openSnack: true,
    message: "",
    alertType: "success"
  })

  const { access_token } = getToken()

  const [participantData, responseUploadParticipants] = useUploadParticipantsMutation()

  const { data = [], isLoading } = useGetAllEventsQuery(access_token)

  const [participantsFileData, setParticipantsFileData] = React.useState({
    event_id: "",
    participants_file: null,
  });

  function handleCloseSnackbar() {
    setSnackAndSpinner({ openSnack: false });
  }

  React.useEffect(() => {
    if (!props.open) {
      setParticipantsFileData({ event_id: "", participants_file: null })
    }
  }, [props.open])

  return (
    <>
      {
        responseUploadParticipants.isLoading ?
          <>
            <BackdropSpinner open={snackAndSpinner.openSpinner} />
          </> : <div className="w-full">
            <Dialog {...props}>
              <DialogTitle>Upload File</DialogTitle>
              <FormControl sx={{ minWidth: 400, margin: 2, gap: 2 }}>
                <InputLabel id="events">Choose Event</InputLabel>
                <Select
                  labelId="events"
                  id='event_id'
                  name="event_id"
                  value={participantsFileData.event_id}
                  variant="standard"
                  type="text"
                  label="Events"
                  onChange={(e) => { setParticipantsFileData({ ...participantsFileData, event_id: e.target.value }) }}
                >
                  {data !== undefined ? (
                    Object.values(data).map((events) => {
                      return (
                        <MenuItem value={events.id} key={events.id} >
                          {
                            isLoading ? <LoaderSkeleton barWidth={"10px"} /> : events.event_name
                          }
                        </MenuItem>
                      );
                    })
                  ) : (
                    <MenuItem value={null} key={null}>
                      No Data Available
                    </MenuItem>
                  )}
                </Select>
                <TextField
                  inputProps={{ accept: ".xlsx, .xls" }}
                  onChange={(e) => { setParticipantsFileData({ ...participantsFileData, participants_file: e.target.files[0] }) }}
                  autoFocus
                  margin="dense"
                  id="participants_file"
                  type='file'
                  fullWidth
                  variant="standard"
                />
              </FormControl>
              <DialogActions>
                <Button onClick={props.onClose}>Cancel</Button>
                <Button onClick={() => { participantData({ access_token: access_token, participantsFileData: participantsFileData }); setParticipantsFileData({ event_id: "", participants_file: null }) }}>Upload File</Button>
              </DialogActions>
            </Dialog>
            {
              responseUploadParticipants.data ?
                <AlertSnackbar
                  open={snackAndSpinner.openSnack}
                  message={responseUploadParticipants.data}
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
