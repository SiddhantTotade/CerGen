import * as React from "react";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import { Button } from "@mui/material";
import Webcam from 'react-webcam'
import axios from "axios";

const videoConstraints = {
    width: 1280,
    height: 720,
    facingMode: "environment"
};

export default function ParticipantImage(props) {
    const webCamRef = React.useRef(null)
    const [imgSrc, setImgSrc] = React.useState(null)
    const capture = React.useCallback(
        () => {
            const imageSrc = webCamRef.current.getScreenshot({ width: 1920, height: 1080 });
            setImgSrc(imageSrc)
        },
        [webCamRef, setImgSrc]
    );

    function handleImageUpload(e) {
        e.preventDefault()
        const url = 'http://127.0.0.1:8000/api/upload-participant-image/' + props.participant.event

        const formData = new FormData()
        formData.append('participant_image', imgSrc)

        axios.put(url, formData, { headers: { "Authorization": "Token " + localStorage.getItem("token") } }).then(res => console.log(res.data))
    }

    return (
        <Dialog {...props} maxWidth='lg' >
            <DialogTitle>Take Photo</DialogTitle>
            <DialogContent sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: "10px" }}>
                <div className="w-2/4">
                    <Webcam
                        audio={false}
                        height={720}
                        ref={webCamRef}
                        screenshotFormat="image/jpeg"
                        width={1280}
                        videoConstraints={videoConstraints}
                    />
                </div>
                <div className="w-2/4">
                    <img src={imgSrc} alt="" />
                </div>
            </DialogContent>
            <DialogActions sx={{ display: 'flex', justifyContent: 'space-between' }}>
                <div className="mb-2 ml-1">
                    <Button onClick={capture} sx={{ background: '#e81551', color: 'white', ':hover': { background: '#c70841' } }} >Click Photo</Button>
                </div>
                <div className="flex gap-3 mr-1 mb-2">
                    <Button onClick={props.onClose} variant='contained'>Cancel</Button>
                    <Button onClick={handleImageUpload} variant='contained' >Upload Photo</Button>
                </div>
            </DialogActions>
        </Dialog>
    );
}
