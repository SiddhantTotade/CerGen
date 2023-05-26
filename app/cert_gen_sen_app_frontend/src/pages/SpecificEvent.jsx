import * as React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import Sidebar from "../components/base_components/Sidebar";
import { useState } from "react";
import DoneIcon from "@mui/icons-material/Done";
import CloseIcon from "@mui/icons-material/Close";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import CameraAltIcon from '@mui/icons-material/CameraAlt';
import InsertPhotoIcon from '@mui/icons-material/InsertPhoto';
import SendIcon from "@mui/icons-material/Send";
import { Button, Typography, Box } from "@mui/material";
import Tooltip from "@mui/material/Tooltip";
import CreateParticipant from "../components/participant_components/CreateParticipant";
import UpdateParticipant from "../components/participant_components/UpdateParticipant";
import DeleteParticipant from "../components/participant_components/DeleteParticipant";
import CertificateTemplate from "../components/template_components/CertificateTemplate";
import GenerateCertificate from "../components/certficate_components/GenerateCertificate";
import GenerateCertificateById from "../components/certficate_components/GenerateCertificateById";
import Gold from "../medals_images/gold-medal.png";
import Silver from "../medals_images/silver-medal.png";
import Bronze from "../medals_images/bronze-medal.png";
import ParticipantImage from "../components/participant_components/ParticipantImage";
import AlbumForm from "../components/image_components/AlbumForm";
import LoaderSkeleton from "../components/base_components/LoaderSkeleton";
import { getToken } from "../services/LocalStorageService";
import { useGetParticipantsQuery } from "../services/participantsAPI";
import { useSpecificEventDetailQuery } from "../services/eventsAPI";
import DownloadIcon from '@mui/icons-material/Download';
import axios from "axios";
import InputBase from '@mui/material/InputBase';
import { styled, alpha } from '@mui/material/styles';
import SearchIcon from '@mui/icons-material/Search';

const Search = styled('div')(({ theme }) => ({
  position: 'relative',
  borderRadius: theme.shape.borderRadius,
  border: "1px solid gainsboro",
  backgroundColor: alpha(theme.palette.common.white, 0.15),
  '&:hover': {
    backgroundColor: alpha(theme.palette.common.white, 0.25),
  },
  marginLeft: 0,
  width: '100%',
  [theme.breakpoints.up('sm')]: {
    marginLeft: theme.spacing(3),
    width: 'auto',
  },
}));

const SearchIconWrapper = styled('div')(({ theme }) => ({
  padding: theme.spacing(0, 2),
  color: "gray",
  height: '100%',
  position: 'absolute',
  pointerEvents: 'none',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
}));

const StyledInputBase = styled(InputBase)(({ theme }) => ({
  color: 'inherit',
  '& .MuiInputBase-input': {
    padding: theme.spacing(1, 1, 1, 0),
    // vertical padding + font size from searchIcon
    paddingLeft: `calc(1em + ${theme.spacing(4)})`,
    transition: theme.transitions.create('width'),
    width: '100%',
    [theme.breakpoints.up('md')]: {
      width: '30ch',
    },
  },
}));

const createBtns = {
  marginBottom: "10px",
  marginRight: "10px",
};

const tableRow = 6

const tableSkeleton = [...Array(tableRow)].map((e, i) =>
  <TableBody key={i}>
    <TableRow>
      <TableCell><LoaderSkeleton barWidth={150} barPadding={2} /></TableCell>
      <TableCell><LoaderSkeleton barWidth={150} barPadding={2} /></TableCell>
      <TableCell><LoaderSkeleton barWidth={150} barPadding={2} /></TableCell>
      <TableCell><LoaderSkeleton barWidth={150} barPadding={2} /></TableCell>
      <TableCell><LoaderSkeleton barWidth={50} barPadding={2} /></TableCell>
      <TableCell><LoaderSkeleton barWidth={50} barPadding={2} /></TableCell>
      <TableCell><LoaderSkeleton barWidth={70} barPadding={2} /></TableCell>
    </TableRow>
  </TableBody>
)

export default function SpecificEvent() {

  const event_url = window.location.href;
  let event_slug = "";

  for (let i = event_url.length - 1; i > 0; i--) {
    event_slug += event_url[i];
    if (event_url[i] === "/") {
      break;
    }
  }

  const ReverseString = (event_slug) => [...event_slug].reverse().join("");
  event_slug = ReverseString(event_slug.replace("/", ""));

  const { access_token } = getToken()

  const { data = [], isLoading } = useGetParticipantsQuery({ access_token: access_token, event_slug: event_slug })

  const eventData = useSpecificEventDetailQuery({ access_token: access_token, event_slug: event_slug })

  const [specificEventDetails, setSpecificEventDetails] = useState({})

  const [participantDetails, setParticipantsDetails] = useState({
    id: "",
    event: "",
    participant_name: "",
    participant_id: "",
    email: "",
    phone: "",
    certificate_status: "",
    certificate_id: "",
    certificate_sent_status: "",
    participant_img: "",
  });

  let attendance = 0;

  const [createParticiapantForm, setCreateParticiapantForm] =
    React.useState(false);

  const [uploadTemplateForm, setUploadTemplateForm] = React.useState(false);

  const [updateForm, setUpdateForm] = useState(false);

  const [deleteForm, setDeleteForm] = useState(false);

  const [album, setAlbum] = useState(false)

  const [camera, setCamera] = useState(false)

  const [generateCertificateForm, setGenerateCertificateForm] = useState(false)

  const [generateCertificateByIdForm, setGenerateCertificateByIdForm] = useState(false)

  const [value, setValue] = useState('')
  const [dataSource, setDataSource] = useState(data)
  const [tableFilter, setTableFilter] = useState([])

  const handleSearch = (e) => {
    if (e !== "") {
      setValue(e)
      const filterTable = data.filter(o => Object.keys(o).some(k => String(o[k]).toLowerCase().includes(e.toLowerCase())))
      setTableFilter([...filterTable])
    }
    else {
      setValue(e)
      setDataSource([...dataSource])
    }
  }

  React.useEffect(() => {
    if (!eventData.isLoading) {
      setSpecificEventDetails(eventData.data[0])
    }
  }, [eventData.data, eventData.isLoading])

  const handleGenerateCertificateForm = () => {
    setGenerateCertificateForm(true)
  }

  const handleGenerateCertificateFormClose = () => {
    setGenerateCertificateForm(false)
  }

  const handleGenerateCertificateByIdForm = (id) => {
    setParticipantsDetails({ id: id })
    setGenerateCertificateByIdForm(true)
  }

  const handleGenerateCertificateFormByIdClose = () => {
    setGenerateCertificateByIdForm(false)
  }

  const handleAlbumForm = () => {
    setAlbum(true)
  }

  const handleAlbumFormClose = () => {
    setAlbum(false)
  }

  const handleCameraForm = (id, img) => {
    setCamera(true)
    setParticipantsDetails({ participant_img: img, id: id })
  }

  const handleImageForm = (id, img) => {
    setCamera(true)
    setParticipantsDetails({ participant_img: img, id: id })
  }

  const handleCameraFormClose = () => {
    setCamera(false);
    setParticipantsDetails("")
  };

  const handleUploadTemplateForm = () => {
    setUploadTemplateForm(true);
  };

  const handleUploadTemplateFormClose = () => {
    setUploadTemplateForm(false);
  };

  const handleForm = () => {
    setCreateParticiapantForm(true);
  };

  const handleFormClose = () => {
    setCreateParticiapantForm(false);
  };

  const handleUpdateForm = (
    id,
    event,
    participant_name,
    participant_id,
    email,
    phone,
    certificate_status,
    certificate_id,
    certificate_sent_status,
    participant_img
  ) => {
    setUpdateForm(true);
    setParticipantsDetails({ id: id, event: event, participant_name: participant_name, participant_id: participant_id, email: email, phone: phone, certificate_status: certificate_status, certificate_id: certificate_id, certificate_sent_status: certificate_sent_status, participant_img: participant_img })
  };

  const handleUpdateFormClose = () => {
    setUpdateForm(false);
  };

  const handleDeleteForm = (id, participant_name) => {
    setDeleteForm(true);
    setParticipantsDetails({ id: id, participant_name: participant_name })
  };

  const handleDeleteFormClose = () => {
    setDeleteForm(false);
  };

  const forceDownload = (file, file_name) => {
    const url = window.URL.createObjectURL(new Blob([file.data]))
    const link = document.createElement("a")
    link.href = url
    link.setAttribute('download', file_name)
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
  }

  const downloadCertificate = (file_url, file_name) => {
    const fileUrl = 'http://127.0.0.1:8000' + file_url

    axios({
      method: "GET",
      url: fileUrl,
      responseType: 'arraybuffer'
    }).then((res) => {
      forceDownload(res, file_name)
    }).catch((err) => console.log(err))
  }

  function checkDownloadCertificate() {
    if (eventData.data) {
      if (eventData.data[0]['certificates_file'] === null) {
        return false

      }
      else {
        return true
      }
    }
    else {
      return false
    }
  }

  return (
    <div className="flex justify-center items-center">
      {
        checkDownloadCertificate() ?
          <Box sx={{ position: 'absolute', zIndex: '15000', marginRight: '1400px', marginTop: '-300px' }}>
            <Tooltip title="Download Certificate"><Button variant="contained" sx={{ borderRadius: '100px' }} onClick={() => downloadCertificate(eventData.data[0]['certificates_file'], eventData.data[0]['certificate_file_name'])} ><DownloadIcon /></Button></Tooltip>
          </Box> : ""
      }
      <Sidebar />
      <div className="w-3/4 mt-24">
        <Box sx={{
          display: "flex",
          justifyContent: "space-evenly",
          alignItems: 'center',
          borderBottom: "1px solid gray",
        }}>
          {
            eventData.isLoading ? <><LoaderSkeleton barWidth={500} barPadding={3} /><LoaderSkeleton barWidth={500} barPadding={3} /></> : <>
              <Typography sx={{ fontSize: "40px", }}>{specificEventDetails.event_name}</Typography>
              <Typography sx={{ fontSize: '15px' }}>{specificEventDetails.subject}</Typography>
            </>
          }
        </Box>
        {data.forEach((event) => {
          return event.certificate_status === "T" ||
            event.certificate_status === "1" ||
            event.certificate_status === "2" ||
            event.certificate_status === "3"
            ? attendance++
            : "";
        })}
        <div className="flex justify-between mt-3">
          <small className="text-blue-600">
            Total Participants : {data.length}
          </small>
          <small className="text-green-600">
            Attended Participants : {attendance}
          </small>
          <small className="text-red-600">
            Absent Participants : {data.length - attendance}
          </small>
        </div>
        <div className="flex justify-between gap-10 mt-5">
          <div>
            <Button variant="contained" sx={createBtns} onClick={handleForm}>
              Create Participant
            </Button>
            <Button
              variant="contained"
              sx={createBtns}
              onClick={handleGenerateCertificateForm}
            >
              Issue and Send Certificate
            </Button>
            <Button
              variant="contained"
              sx={createBtns}
              onClick={handleUploadTemplateForm}
            >
              Templates
            </Button>
            <Button
              variant="contained"
              sx={createBtns}
              onClick={handleAlbumForm}
            >
              View Album
            </Button>
          </div>
          <div>
            <Search onChange={(e) => handleSearch(e.target.value)}>
              <SearchIconWrapper>
                <SearchIcon />
              </SearchIconWrapper>
              <StyledInputBase
                placeholder="Search…"
                inputProps={{ 'aria-label': 'search' }}
              />
            </Search>
          </div>
        </div>
        <TableContainer sx={{ height: '65vh', position: 'relative', overflow: 'auto', '::-webkit-scrollbar-thumb': { 'background': '#1976d2', borderRadius: '50px' }, '::-webkit-scrollbar-track': { background: '#f1f1f1' }, '::-webkit-scrollbar': { width: '3px', background: 'transparent' } }} component={Paper}>
          <Table stickyHeader sx={{ minWidth: 450, position: 'sticky' }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell align="center">
                  <b>Participant Name</b>
                </TableCell>
                <TableCell align="center">
                  <b>Participant Id</b>
                </TableCell>
                <TableCell align="center">
                  <b>Participant Email</b>
                </TableCell>
                <TableCell align="center">
                  <b>Participant Phone</b>
                </TableCell>
                <TableCell align="center">
                  <b>Eligible</b>
                </TableCell>
                <TableCell align="center">
                  <b>Photos</b>
                </TableCell>
                <TableCell align="center">
                  <b>Actions</b>
                </TableCell>
              </TableRow>
            </TableHead>
            {
              isLoading ? tableSkeleton :
                <TableBody>
                  {data.length !== 0 ?
                    value.length > 0 ?
                      tableFilter.map((row) => (
                        <TableRow
                          key={row.id}
                          sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
                        >
                          <TableCell align="center">{row.participant_name}</TableCell>
                          <TableCell align="center">{row.participant_id}</TableCell>
                          <TableCell align="center">{row.email}</TableCell>
                          <TableCell align="center">{row.phone}</TableCell>
                          {row.certificate_status === "1" ? (
                            <TableCell
                              align="center"
                              sx={{ display: "flex", justifyContent: "center" }}
                            >
                              <Tooltip
                                className="cursor-pointer"
                                title={
                                  row.certificate_sent_status === true
                                    ? `Certificate sended to ${row.participant_name}`
                                    : `${row.participant_name} is eligible for certificate`
                                }
                              >
                                <img src={Gold} className="w-10" alt="gold medal png" />
                              </Tooltip>
                            </TableCell>
                          ) : row.certificate_status === "2" ? (
                            <TableCell
                              align="center"
                              sx={{ display: "flex", justifyContent: "center" }}
                            >
                              <Tooltip
                                className="cursor-pointer"
                                title={
                                  row.certificate_sent_status === true
                                    ? `Certificate sended to ${row.participant_name}`
                                    : `${row.participant_name} is eligible for certificate`
                                }
                              >
                                <img
                                  src={Silver}
                                  className="w-10"
                                  alt="silver medal png"
                                />
                              </Tooltip>
                            </TableCell>
                          ) : row.certificate_status === "3" ? (
                            <TableCell
                              align="center"
                              sx={{ display: "flex", justifyContent: "center" }}
                            >
                              <Tooltip
                                className="cursor-pointer"
                                title={
                                  row.certificate_sent_status === true
                                    ? `Certificate sended to ${row.participant_name}`
                                    : `${row.participant_name} is eligible for certificate`
                                }
                              >
                                <img
                                  src={Bronze}
                                  className="w-10"
                                  alt="bronze medal png"
                                />
                              </Tooltip>
                            </TableCell>
                          ) : row.certificate_status === "T" ? (
                            <TableCell align="center">
                              <Tooltip
                                className="cursor-pointer"
                                title={
                                  row.certificate_sent_status === true
                                    ? `Certificate sended to ${row.participant_name}`
                                    : `${row.participant_name} is eligible for certificate`
                                }
                              >
                                <DoneIcon sx={{ color: "green" }} />
                              </Tooltip>
                            </TableCell>
                          ) : (
                            <TableCell align="center">
                              <Tooltip
                                className="cursor-pointer"
                                title={`${row.participant_name} is not eligible for certificate`}
                              >
                                <CloseIcon sx={{ color: "red" }} />
                              </Tooltip>
                            </TableCell>
                          )}{
                            row.participant_image === null ?
                              <TableCell align="center">
                                <Tooltip title={`Click / Upload a photo of : ${row.participant_name}`}>
                                  <Button onClick={() => handleCameraForm(row.id, row.participant_image)}>
                                    <CameraAltIcon sx={{ color: '#e81551' }} />
                                  </Button>
                                </Tooltip>
                              </TableCell> :
                              <TableCell align="center">
                                <Tooltip title={`View / Update photo of : ${row.participant_name}`}>
                                  <Button onClick={() => handleImageForm(row.id, row.participant_image)}>
                                    <InsertPhotoIcon sx={{ color: '#1f0abf' }} />
                                  </Button>
                                </Tooltip>
                              </TableCell>
                          }
                          {row.certificate_sent_status === false ? (
                            <TableCell align="center">
                              <Tooltip title={`Edit : ${row.participant_name}`}>
                                <Button
                                  onClick={() =>
                                    handleUpdateForm(
                                      row.id,
                                      row.event,
                                      row.participant_name,
                                      row.participant_id,
                                      row.email,
                                      row.phone,
                                      row.certificate_status,
                                      row.certificate_id,
                                      row.certificate_sent_status,
                                      row.participant_img
                                    )
                                  }
                                  key={row.id}
                                >
                                  <EditIcon sx={{ color: "blue" }} />
                                </Button>
                              </Tooltip>
                              <Tooltip title={`Delete : ${row.participant_name}`}>
                                <Button onClick={() => handleDeleteForm(row.id, row.participant_name)}>
                                  <DeleteIcon sx={{ color: "red" }} />
                                </Button>
                              </Tooltip>
                              <Tooltip title={`Send Certificate : ${row.email}`}>
                                <Button
                                  onClick={() => handleGenerateCertificateByIdForm(row.id)}
                                >
                                  <SendIcon sx={{ color: "grey" }} />
                                </Button>
                              </Tooltip>
                            </TableCell>
                          ) : (
                            <TableCell align="center"></TableCell>
                          )}
                        </TableRow>
                      )) :
                      data.map((row) => (
                        <TableRow
                          key={row.id}
                          sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
                        >
                          <TableCell align="center">{row.participant_name}</TableCell>
                          <TableCell align="center">{row.participant_id}</TableCell>
                          <TableCell align="center">{row.email}</TableCell>
                          <TableCell align="center">{row.phone}</TableCell>
                          {row.certificate_status === "1" ? (
                            <TableCell
                              align="center"
                              sx={{ display: "flex", justifyContent: "center" }}
                            >
                              <Tooltip
                                className="cursor-pointer"
                                title={
                                  row.certificate_sent_status === true
                                    ? `Certificate sended to ${row.participant_name}`
                                    : `${row.participant_name} is eligible for certificate`
                                }
                              >
                                <img src={Gold} className="w-10" alt="gold medal png" />
                              </Tooltip>
                            </TableCell>
                          ) : row.certificate_status === "2" ? (
                            <TableCell
                              align="center"
                              sx={{ display: "flex", justifyContent: "center" }}
                            >
                              <Tooltip
                                className="cursor-pointer"
                                title={
                                  row.certificate_sent_status === true
                                    ? `Certificate sended to ${row.participant_name}`
                                    : `${row.participant_name} is eligible for certificate`
                                }
                              >
                                <img
                                  src={Silver}
                                  className="w-10"
                                  alt="silver medal png"
                                />
                              </Tooltip>
                            </TableCell>
                          ) : row.certificate_status === "3" ? (
                            <TableCell
                              align="center"
                              sx={{ display: "flex", justifyContent: "center" }}
                            >
                              <Tooltip
                                className="cursor-pointer"
                                title={
                                  row.certificate_sent_status === true
                                    ? `Certificate sended to ${row.participant_name}`
                                    : `${row.participant_name} is eligible for certificate`
                                }
                              >
                                <img
                                  src={Bronze}
                                  className="w-10"
                                  alt="bronze medal png"
                                />
                              </Tooltip>
                            </TableCell>
                          ) : row.certificate_status === "T" ? (
                            <TableCell align="center">
                              <Tooltip
                                className="cursor-pointer"
                                title={
                                  row.certificate_sent_status === true
                                    ? `Certificate sended to ${row.participant_name}`
                                    : `${row.participant_name} is eligible for certificate`
                                }
                              >
                                <DoneIcon sx={{ color: "green" }} />
                              </Tooltip>
                            </TableCell>
                          ) : (
                            <TableCell align="center">
                              <Tooltip
                                className="cursor-pointer"
                                title={`${row.participant_name} is not eligible for certificate`}
                              >
                                <CloseIcon sx={{ color: "red" }} />
                              </Tooltip>
                            </TableCell>
                          )}{
                            row.participant_image === null ?
                              <TableCell align="center">
                                <Tooltip title={`Click / Upload a photo of : ${row.participant_name}`}>
                                  <Button onClick={() => handleCameraForm(row.id, row.participant_image)}>
                                    <CameraAltIcon sx={{ color: '#e81551' }} />
                                  </Button>
                                </Tooltip>
                              </TableCell> :
                              <TableCell align="center">
                                <Tooltip title={`View / Update photo of : ${row.participant_name}`}>
                                  <Button onClick={() => handleImageForm(row.id, row.participant_image)}>
                                    <InsertPhotoIcon sx={{ color: '#1f0abf' }} />
                                  </Button>
                                </Tooltip>
                              </TableCell>
                          }
                          {row.certificate_sent_status === false ? (
                            <TableCell align="center">
                              <Tooltip title={`Edit : ${row.participant_name}`}>
                                <Button
                                  onClick={() =>
                                    handleUpdateForm(
                                      row.id,
                                      row.event,
                                      row.participant_name,
                                      row.participant_id,
                                      row.email,
                                      row.phone,
                                      row.certificate_status,
                                      row.certificate_id,
                                      row.certificate_sent_status,
                                      row.participant_img
                                    )
                                  }
                                  key={row.id}
                                >
                                  <EditIcon sx={{ color: "blue" }} />
                                </Button>
                              </Tooltip>
                              <Tooltip title={`Delete : ${row.participant_name}`}>
                                <Button onClick={() => handleDeleteForm(row.id, row.participant_name)}>
                                  <DeleteIcon sx={{ color: "red" }} />
                                </Button>
                              </Tooltip>
                              <Tooltip title={`Send Certificate : ${row.email}`}>
                                <Button
                                  onClick={() => handleGenerateCertificateByIdForm(row.id)}
                                >
                                  <SendIcon sx={{ color: "grey" }} />
                                </Button>
                              </Tooltip>
                            </TableCell>
                          ) : (
                            <TableCell align="center"></TableCell>
                          )}
                        </TableRow>
                      ))
                    : (
                      <TableRow
                        sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
                      >
                        <TableCell align="center">No Data</TableCell>
                      </TableRow>
                    )}
                </TableBody>
            }
          </Table>
        </TableContainer>
        <CreateParticipant
          open={createParticiapantForm}
          onClose={handleFormClose}
          participant={participantDetails}
          event_slug={event_slug.toUpperCase()}
          event_detail={specificEventDetails}
        />
        <UpdateParticipant
          open={updateForm}
          onClose={handleUpdateFormClose}
          participant={participantDetails}
          event_slug={event_slug.toUpperCase()}
          event_detail={specificEventDetails}
        />
        <DeleteParticipant
          open={deleteForm}
          onClose={handleDeleteFormClose}
          participant={participantDetails}
        />
        <CertificateTemplate
          open={uploadTemplateForm}
          onClose={handleUploadTemplateFormClose}
        />
        <GenerateCertificate open={generateCertificateForm} onClose={handleGenerateCertificateFormClose} event={eventData.data} />
        <GenerateCertificateById open={generateCertificateByIdForm} onClose={handleGenerateCertificateFormByIdClose} event={eventData.data} participant={participantDetails} />
        <ParticipantImage open={camera} onClose={handleCameraFormClose} participant={participantDetails} />
        <AlbumForm open={album} onClose={handleAlbumFormClose} participant={participantDetails} event_slug={event_slug} />
      </div>
    </div>
  );
}
