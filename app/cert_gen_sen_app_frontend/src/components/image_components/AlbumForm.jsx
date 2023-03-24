import * as React from "react";
import Dialog from "@mui/material/Dialog";
import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import CloseIcon from '@mui/icons-material/Close';
import { useEffect } from "react";
import axios from "axios";

export default function AlbumForm(props) {

    const [album, setAlbum] = React.useState("")

    useEffect(() => {
        const url = ""

        axios.get(url, {
            headers: { Authorization: "Token " + localStorage.getItem("token") },
        }).then(res => console.log(res)).catch(err => console.log(err))
    })

    return (
        <div className="w-full">
            <Dialog {...props}>
                <DialogTitle sx={{ display: 'flex', justifyContent: 'space-between' }}>
                    <div>Add Participant</div>
                    <div><CloseIcon sx={{ color: 'gray' }} /></div>
                </DialogTitle>
                <DialogContent>
                </DialogContent>
            </Dialog >
        </div >
    );
}
