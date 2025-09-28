import React, { useState } from 'react'
import Webcam from 'react-webcam'
import { DialogActions, Button, Paper } from '@mui/material';
import { useUploadParticipantImageMutation } from '../../services/participantsImagesAPI';
import { getToken } from '../../services/LocalStorageService';
import AlertBar from '../base_components/AlertBar';
import { CircularProgress } from '@mui/material';

const videoConstraints = {
    width: 1280,
    height: 720,
    facingMode: "environment"
};

export const Camera = (props) => {

    const { access_token } = getToken()

    const [uploadParticipantImage, responsePaticipantImage] = useUploadParticipantImageMutation()

    const [reClick, setReClick] = useState(false)

    const webCamRef = React.useRef(null)

    const [imgSrc, setImgSrc] = React.useState(null)

    const [imageValidation, setImageValidation] = useState(false)

    const capture = React.useCallback(
        () => {
            const imageSrc = webCamRef.current.getScreenshot({ width: 1920, height: 1080 });
            setImgSrc(imageSrc)
        },
        [webCamRef, setImgSrc]
    );

    const Webcamera = <div className='flex w-full gap-5 justify-center'>
        <div className='w-2/4'>
            <Webcam
                audio={false}
                height={720}
                ref={webCamRef}
                screenshotFormat="image/jpeg"
                width={1280}
                mirrored={true}
                videoConstraints={videoConstraints}
            />
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

    const UploadedImage =
        <div className="flex justify-center">
            <div className='flex justify-center w-2/4'>
                <Paper elevation={12}
                    style={{
                        width: "100%",
                        height: "100%",
                        display: 'flex',
                        justifyContent: 'center',
                        alignItems: 'center'
                    }}>
                    <img src={'http://127.0.0.1:8000' + props.participant.participant_img} alt='Preview' width={700} />
                </Paper>
            </div>
        </div>

    const ClickPhoto = <div className='flex gap-4'>
        <Button onClick={capture} sx={{ background: '#e81551', color: 'white', ':hover': { background: '#c70841' } }} >Click Photo</Button>
        {
            imageValidation === true ? <AlertBar message="Please click an image before upload" severity="error" /> : ""
        }
    </div>

    function handleImageUpload(e) {
        e.preventDefault()
        if (imgSrc === null) {
            setImageValidation(true)
            setTimeout(() => {
                setImageValidation(false)
            }, 2000)
        }
        else {
            uploadParticipantImage({ access_token: access_token, imgSrc: imgSrc, event: props.participant.event })
        }
    }

    function handleImage() {
        reClick === true ? setReClick(false) : setReClick(true)
    }

    return (
        <div>
            {props.participant.participant_img === null ? Webcamera : reClick === true ? Webcamera : UploadedImage}
            {
                responsePaticipantImage.isLoading ? <CircularProgress /> :
                    <DialogActions sx={{ display: 'flex', justifyContent: 'space-between', marginTop: '10px' }}>
                        {reClick === true ? ClickPhoto : props.participant.participant_img === "" ?
                            ClickPhoto :
                            <div>
                                <Button onClick={handleImage} sx={{ background: '#e81551', color: 'white', ':hover': { background: '#c70841' } }} >ReClick</Button>
                            </div>
                        }
                        <div className="flex gap-3">
                            <Button onClick={props.onClose} variant='contained'>Cancel</Button>
                            <Button onClick={handleImageUpload} variant='contained' >Upload Photo</Button>
                        </div>
                    </DialogActions >
            }
        </div >
    )
}
