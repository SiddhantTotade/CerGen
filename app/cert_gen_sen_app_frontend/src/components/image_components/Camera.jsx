import React from 'react'
import Webcam from 'react-webcam'
import { DialogActions, Button, Paper } from '@mui/material';
import axios from 'axios';

const videoConstraints = {
    width: 1280,
    height: 720,
    facingMode: "environment"
};

export const Camera = (props) => {
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

        axios.patch(url, formData, { headers: { "Authorization": "Token " + localStorage.getItem("token") } }).then(res => console.log(res.data))
    }

    return (
        <div>
            <div className='flex w-full gap-5'>
                <div className='w-2/4'>
                    {props.participant.student_img === "" ?
                        <Webcam
                            audio={false}
                            height={720}
                            ref={webCamRef}
                            screenshotFormat="image/jpeg"
                            width={1280}
                            mirrored={true}
                            videoConstraints={videoConstraints}
                        /> :
                        <img src={props.participant.student_img} alt='Preview' />
                    }
                </div>
                <div className='w-2/4'>
                    <Paper elevation={12}
                        style={{
                            width: "100%",
                            height: "100%",
                            display: 'flex',
                            justifyContent: 'center',
                            alignItems: 'center'
                        }}>
                        <img src={imgSrc} alt="" />
                    </Paper>
                </div>
            </div>
            <DialogActions sx={{ display: 'flex', justifyContent: 'space-between', marginTop: '10px' }}>
                <div className="">
                    <Button onClick={capture} sx={{ background: '#e81551', color: 'white', ':hover': { background: '#c70841' } }} >Click Photo</Button>
                </div>
                <div className="flex gap-3">
                    <Button onClick={props.onClose} variant='contained'>Cancel</Button>
                    <Button onClick={handleImageUpload} variant='contained' >Upload Photo</Button>
                </div>
            </DialogActions>
        </div>
    )
}
