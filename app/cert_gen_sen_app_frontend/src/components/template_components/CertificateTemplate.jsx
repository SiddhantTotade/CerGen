import * as React from "react";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";
import { Box, Tab } from "@mui/material";
import PropTypes from "prop-types";
import { Tabs } from "@mui/material";
import { UploadTemplate } from "./UploadTemplate";
import { ChooseCompletionTemplate } from "./ChooseCompletionTemplate";
import { ChooseMeritTemplate } from "./ChooseMeritCertificate";

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

export default function CertificateTemplate(props) {

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
              <Tab label="Choose Participantion Template" {...a11yProps(0)} />
              <Tab label="Choose Merit Template" {...a11yProps(1)} />
              <Tab label="Upload Template" {...a11yProps(2)} />
            </Tabs>
          </Box>
          <TabPanel value={value} index={0}>
            <ChooseCompletionTemplate props={props} />
          </TabPanel>
          <TabPanel value={value} index={1}>
            <ChooseMeritTemplate props={props} />
          </TabPanel>
          <TabPanel value={value} index={2}>
            <UploadTemplate props={props} />
          </TabPanel>
        </Box>
      </Dialog>
    </div>
  );
}
