import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Sidebar from '../base_components/Sidebar'
import axios from 'axios';
import { useState, useEffect } from 'react';
import DoneIcon from '@mui/icons-material/Done';
import CloseIcon from '@mui/icons-material/Close';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import SendIcon from '@mui/icons-material/Send';
import { Button } from '@mui/material';
import Tooltip from '@mui/material/Tooltip';
import CreateParticipant from '../participant_components/CreateParticipant';
import UpdateParticipant from '../participant_components/UpdateParticipant';
import DeleteParticipant from '../participant_components/DeleteParticipant';
import Gold from '../medals_images/gold-medal.png'
import Silver from '../medals_images/silver-medal.png'
import Bronze from '../medals_images/bronze-medal.png'

const createBtns = {
    background: '#3293a8',
    color: 'white',
    marginBottom: '10px',
    marginRight: '10px',
    '&:hover': {
        background: "#327fa8",
    }
}

export default function SpecificEvent() {

    const [eventsData, setEventsData] = useState([])
    const [participantDetails] = useState({
        event: "",
        student_name: "",
        student_id: "",
        email: "",
        certificate_status: ""

    })

    const event_url = window.location.href

    useEffect(() => {

        const new_event_url = event_url.replace("3000", "8000")

        const fetchData = async () => {
            try {
                const response = await axios.get(new_event_url)
                setEventsData(response.data)
            }
            catch (error) {
                console.log(error);
            }
        }
        fetchData()
    }, [eventsData])

    let event_slug = ""

    for (let i = event_url.length - 1; i > 0; i--) {
        event_slug += event_url[i]
        if (event_url[i] === "/") {
            break
        }
    }

    const ReverseString = event_slug => [...event_slug].reverse().join('');
    event_slug = ReverseString(event_slug.replace("/", ""))

    const generateCertificate = async () => {

        const url = 'http://127.0.0.1:8000/api/generate-certificate/' + event_slug

        const certificateData = async () => {

            try {
                const response = await axios.get(url)
                setEventsData(response.data)
            }
            catch (error) {
                console.log(error);
            }
        }
        certificateData()
    }

    const generateCertificateById = async (id) => {

        const url = 'http://127.0.0.1:8000/api/generate-certificate/' + event_slug + "/" + id

        const certificateData = async () => {

            try {
                const response = await axios.get(url).then(res => console.log(res))
                setEventsData(response.data)
            }
            catch (error) {
                console.log(error);
            }
        }
        certificateData()
    }

    const [form, setForm] = React.useState(false)
    const [updateForm, setUpdateForm] = useState(false)
    const [deleteForm, setDeleteForm] = useState(false)

    const handleForm = () => {
        setForm(true);
    }

    const handleFormClose = () => {
        setForm(false);
    }

    const handleUpdateForm = (id, student_name, student_id, email, certificate_status) => {
        setUpdateForm(true);
        participantDetails.event = id
        participantDetails.student_name = student_name
        participantDetails.student_id = student_id
        participantDetails.email = email
        participantDetails.certificate_status = certificate_status
    }

    const handleUpdateFormClose = () => {
        setUpdateForm(false);
    }

    const handleDeleteForm = (id) => {
        setDeleteForm(true);
        participantDetails.event = id
    }

    const handleDeleteFormClose = () => {
        setDeleteForm(false);
    }

    return (
        <div className='flex justify-center items-center'>
            <Sidebar />
            <div className='w-3/5 mt-32'>
                <div className='gap-10'>
                    <Button sx={createBtns} onClick={handleForm}>Create Participant</Button>
                    <Button sx={createBtns} onClick={generateCertificate} >Issue and Send Certificate</Button>
                </div>
                <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 450 }} aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell align='center'><b>Student Name</b></TableCell>
                                <TableCell align='center'><b>Student Id</b></TableCell>
                                <TableCell align='center'><b>Student Email</b></TableCell>
                                <TableCell align='center'><b>Certificate Status</b></TableCell>
                                <TableCell align='center'><b>Actions</b></TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {
                                eventsData !== '0' ?
                                    Object.values(eventsData).map((row) => (
                                        <TableRow key={row.id} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                                            <TableCell align="center">{row.student_name}</TableCell>
                                            <TableCell align="center">{row.student_id}</TableCell>
                                            <TableCell align="center">{row.email}</TableCell>
                                            {row.certificate_status === '1' ?
                                                <TableCell align="center" sx={{ display: 'flex', justifyContent: 'center' }}><img src={Gold} className="w-10" alt="gold medal png" /></TableCell> : row.certificate_status === '2' ? <TableCell align="center" sx={{ display: 'flex', justifyContent: 'center' }}><img src={Silver} className="w-10" alt="silver medal png" /></TableCell> : row.certificate_status === '3' ? <TableCell align="center" sx={{ display: 'flex', justifyContent: 'center' }}><img src={Bronze} className="w-10" alt="bronze medal png" /></TableCell> : row.certificate_status === 'T' ? <TableCell align="center"><DoneIcon sx={{ color: 'green' }} /></TableCell> : <TableCell align="center"><CloseIcon sx={{ color: 'red' }} /></TableCell>
                                            }
                                            {/* {row.certificate_status === '1' ?
                                                <TableCell align="center"><Gold /></TableCell> : <TableCell align="center"><Bronze /></TableCell>
                                            } */}

                                            <TableCell align="center" sx={{}}>
                                                <Tooltip title={`Edit : ${row.id}`} ><Button onClick={() => handleUpdateForm(row.id, row.student_name, row.student_id, row.email, row.certificate_status)} key={row.id} ><EditIcon sx={{ color: "blue" }} /></Button></Tooltip>
                                                <Tooltip title={`Delete : ${row.id}`} ><Button onClick={() => handleDeleteForm(row.id)} ><DeleteIcon sx={{ color: "red" }} /></Button></Tooltip>
                                                <Tooltip title={`Send Certificate : ${row.email}`} ><Button onClick={() => generateCertificateById(row.id)}><SendIcon sx={{ color: "grey" }} /></Button></Tooltip>
                                            </TableCell>
                                        </TableRow>
                                    ))
                                    : <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                                        <TableCell align="center">No Data</TableCell>
                                    </TableRow>
                            }
                        </TableBody>
                    </Table>
                </TableContainer>
                <CreateParticipant open={form} onClose={handleFormClose} />
                <UpdateParticipant open={updateForm} onClose={handleUpdateFormClose} participant={participantDetails} />
                <DeleteParticipant open={deleteForm} onClose={handleDeleteFormClose} participant={participantDetails} />
            </div>
        </div >
    );
}