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
import { useLocation } from 'react-router-dom';

function createData(name, calories, fat, carbs, protein) {
    return { name, calories, fat, carbs, protein };
}

const rows = [
    createData('Frozen yoghurt', 159, 3),
    createData('Ice cream sandwich', 237, 3),
    createData('Eclair', 262, 16.0),
];

export default function SpecificEvent() {

    const [eventsData, setEventsData] = useState([])

    const url = useLocation()
    const from = url.state

    console.log(from);

    useEffect(() => {

        const fetchData = async () => {
            try {
                const response = await axios.get("")
                setEventsData(response.data)
            }
            catch (error) {
                console.log(error);
            }
        }
        fetchData()
    }, [])

    console.log(eventsData);

    return (
        <div className='flex justify-center items-center'>
            <Sidebar />
            <div className='w-3/5 mt-32'>
                <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 450 }} aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell align='center'><b>Student Name</b></TableCell>
                                <TableCell align='center'><b>Student Email</b></TableCell>
                                <TableCell align='center'><b>Certificate Status</b></TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {rows.map((row) => (
                                <TableRow key={row.name} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                                    <TableCell align="center">{row.calories}</TableCell>
                                    <TableCell align="center">{row.fat}</TableCell>
                                    <TableCell align="center">{row.carbs}</TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </div>
        </div>
    );
}