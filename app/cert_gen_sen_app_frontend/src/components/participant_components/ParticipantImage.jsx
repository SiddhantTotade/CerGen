import * as React from "react";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import { Button, Box, Tab, Tabs } from "@mui/material";
import PropTypes from "prop-types";
import Webcam from 'react-webcam'
import axios from "axios";

function TabPanel(props) {
    const { children, value, index, ...other } = props;

    return (
        <div
            role="tabpanel"
            hidden={value !== index}
            id={`simple-tabpanel-${index}`}
            aria-labelledby={`simple-tab-${index}`}
            {...other}
        >
            {value === index && (
                <Box sx={{ p: 2 }}>
                    <div>{children}</div>
                </Box>
            )}
        </div>
    );
}

TabPanel.propTypes = {
    children: PropTypes.node,
    index: PropTypes.number.isRequired,
    value: PropTypes.number.isRequired,
};

function a11yProps(index) {
    return {
        id: `simple-tab-${index}`,
        "aria-controls": `simple-tabpanel-${index}`,
    };
}

const videoConstraints = {
    width: 1280,
    height: 720,
    facingMode: "environment"
};

export default function ParticipantImage(props) {
    const [value, setValue] = React.useState(0);
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

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };


    return (
        <Dialog {...props} maxWidth='lg' >
            <DialogTitle>Take Photo</DialogTitle>
            <Box sx={{ width: "100%" }}>
                <Box sx={{ borderBottom: 1, borderColor: "divider" }}>
                    <Tabs
                        value={value}
                        onChange={handleChange}
                        aria-label="basic tabs example"
                    >
                        <Tab label="Capture Photo" {...a11yProps(0)} />
                        <Tab label="Upload Photo" {...a11yProps(1)} />
                    </Tabs>
                </Box>
                <TabPanel value={value} index={0}>
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
                </TabPanel>
                <TabPanel value={value} index={1}>
                </TabPanel>
            </Box>
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
