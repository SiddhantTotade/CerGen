import * as React from "react";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";
import { Box, Tab, Tabs } from "@mui/material";
import PropTypes from "prop-types";
import { Album } from "./Album";
import { UploadEventAlbum } from "./UploadEventAlbum";
import '../../index.css'

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

export default function AlbumForm(props) {
    const [value, setValue] = React.useState(0);
    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    return (
        <Dialog {...props} maxWidth='lg' >
            <DialogTitle>Photo</DialogTitle>
            <Box sx={{ width: "100%" }}>
                <Box sx={{ borderBottom: 1, borderColor: "divider" }}>
                    <Tabs
                        value={value}
                        onChange={handleChange}
                        aria-label="basic tabs example"
                    >
                        <Tab label="Event Album" {...a11yProps(0)} />
                        <Tab label="Upload Photo" {...a11yProps(1)} />
                    </Tabs>
                </Box>
                <TabPanel value={value} index={0}>
                    <Album participant={props.participant} onClose={props.onClose} />
                </TabPanel>
                <TabPanel value={value} index={1}>
                    <UploadEventAlbum onClose={props.onClose} event_slug={props.event_slug} />
                </TabPanel>
            </Box>
        </Dialog>
    );
}
