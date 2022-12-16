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
import CreateParticipant from '../participant_components/CreateParticipant';

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
    }, [event_url])

    const [form, setForm] = React.useState(false)

    const handleForm = () => {
        setForm(true);
    }

    const handleFormClose = () => {
        setForm(false);
    }

    return (
        <div className='flex justify-center items-center'>
            <Sidebar />
            <div className='w-3/5 mt-32'>
                <div className='gap-10'>
                    <Button sx={createBtns}>Issue Certificate</Button>
                    <Button sx={createBtns} onClick={handleForm}>Create Participant</Button>
                </div>
                <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 450 }} aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell align='center'><b>Student Name</b></TableCell>
                                <TableCell align='center'><b>Student Email</b></TableCell>
                                <TableCell align='center'><b>Certificate Status</b></TableCell>
                                <TableCell align='center'><b>Actions</b></TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {
                                eventsData !== '0' ?
                                    eventsData.map((row) => (
                                        <TableRow key={row.id} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                                            <TableCell align="center">{row.student_name}</TableCell>
                                            <TableCell align="center">{row.email}</TableCell>
                                            {row.certificate_status === 'F' ?
                                                <TableCell align="center"><DoneIcon sx={{ color: "green" }} /></TableCell> : <TableCell align="center"><CloseIcon sx={{ color: "red" }} /></TableCell>
                                            }
                                            <TableCell align="center" sx={{}}>
                                                <Button><EditIcon sx={{ color: "blue" }} /></Button>
                                                <Button><DeleteIcon sx={{ color: "red" }} /></Button>
                                                <Button><SendIcon sx={{ color: "grey" }} /></Button>
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
            </div>
        </div>
    );
}