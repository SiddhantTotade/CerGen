import * as React from "react";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";
import { Box, Tab } from "@mui/material";
import PropTypes from "prop-types";
import { Tabs } from "@mui/material";

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

export default function UserDetails(props) {

    const [value, setValue] = React.useState(0);

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    return (
        <div>
            <Dialog
                {...props}
                PaperProps={{
                    style: {
                        minWidth: "60%",
                    },
                }}
            >
                <DialogTitle>Templates</DialogTitle>
                <Box sx={{ width: "100%" }}>
                    <Box sx={{ borderBottom: 1, borderColor: "divider" }}>
                        <Tabs
                            value={value}
                            onChange={handleChange}
                            aria-label="basic tabs example"
                        >
                            <Tab label="User Email & Password" {...a11yProps(0)} />
                            <Tab label="Senders Email & Password" {...a11yProps(1)} />
                        </Tabs>
                    </Box>
                    <TabPanel value={value} index={0}>
                        {/* <ChooseCompletionTemplate /> */}
                    </TabPanel>
                    <TabPanel value={value} index={1}>
                        {/* <ChooseMeritTemplate /> */}
                    </TabPanel>
                </Box>
            </Dialog>
        </div>
    );
}
