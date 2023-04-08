import * as React from "react";
import { styled, useTheme } from "@mui/material/styles";
import Box from "@mui/material/Box";
import MuiDrawer from "@mui/material/Drawer";
import MuiAppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import List from "@mui/material/List";
import CssBaseline from "@mui/material/CssBaseline";
import Typography from "@mui/material/Typography";
import Divider from "@mui/material/Divider";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import ChevronRightIcon from "@mui/icons-material/ChevronRight";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import LogoutIcon from "@mui/icons-material/Logout";
import AddCircleOutlineIcon from "@mui/icons-material/AddCircleOutline";
import EventIcon from "@mui/icons-material/Event";
import { Link, useNavigate } from "react-router-dom";
import PersonIcon from "@mui/icons-material/Person";
import EventForm from "../event_components/EventForm";
import FileForm from "../event_components/FileForm";
import FileUploadIcon from "@mui/icons-material/FileUpload";
import BackdropSpinner from "./Backdrop";
import { useState } from "react";
import Footer from "./Footer";
import { Home } from "../../pages/Home";
import "../../pages/styles/home.css";
import { useLocation } from "react-router-dom";
import { useGetLoggedInUserQuery } from "../../services/userAuthAPI";
import { useDispatch, useSelector } from "react-redux";
import { getToken, removeToken } from "../../services/LocalStorageService";
import { unsetUserInfo, setUserInfo } from "../../features/userSlice";
import { unsetUserToken } from "../../features/authSlice";

const drawerWidth = 240;

const openedMixin = (theme) => ({
  width: drawerWidth,
  transition: theme.transitions.create("width", {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.enteringScreen,
  }),
  overflowX: "hidden",
});

const closedMixin = (theme) => ({
  transition: theme.transitions.create("width", {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  overflowX: "hidden",
  width: `calc(${theme.spacing(7)} + 1px)`,
  [theme.breakpoints.up("sm")]: {
    width: `calc(${theme.spacing(8)} + 1px)`,
  },
});

const DrawerHeader = styled("div")(({ theme }) => ({
  display: "flex",
  alignItems: "center",
  justifyContent: "flex-end",
  padding: theme.spacing(0, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
}));

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== "open",
})(({ theme, open }) => ({
  zIndex: theme.zIndex.drawer + 1,
  transition: theme.transitions.create(["width", "margin"], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(open && {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(["width", "margin"], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  }),
}));

const Drawer = styled(MuiDrawer, {
  shouldForwardProp: (prop) => prop !== "open",
})(({ theme, open }) => ({
  width: drawerWidth,
  flexShrink: 0,
  whiteSpace: "nowrap",
  boxSizing: "border-box",
  ...(open && {
    ...openedMixin(theme),
    "& .MuiDrawer-paper": openedMixin(theme),
  }),
  ...(!open && {
    ...closedMixin(theme),
    "& .MuiDrawer-paper": closedMixin(theme),
  }),
}));

const listitem_sx = { display: "block" };

export default function MiniDrawer() {
  const location = useLocation();

  const [form, setForm] = React.useState(false);
  const [csv_form, setCsvForm] = React.useState(false);

  const theme = useTheme();
  const [open, setOpen] = React.useState(false);

  const [openSpinner, setOpenSpinner] = useState(false);

  const navigate = useNavigate()

  const dispatch = useDispatch()

  const myData = useSelector(state => state.user)

  const { access_token } = getToken()

  const { data, isSuccess } = useGetLoggedInUserQuery(access_token)

  const listItemButton_sx = {
    minHeight: 48,
    justifyContent: open ? "initial" : "center",
    px: 2.5,
  };

  const listItemIcon_sx = {
    minWidth: 0,
    mr: open ? 3 : "auto",
    justifyContent: "center",
  };

  const handleDrawerOpen = () => {
    setOpen(true);
  };

  const handleDrawerClose = () => {
    setOpen(false);
  };

  const handleForm = () => {
    setForm(true);
  };

  const handleFormClose = () => {
    setForm(false);
  };

  const handleCsvForm = () => {
    setCsvForm(true);
  };

  const handleCsvFormClose = () => {
    setCsvForm(false);
  };

  const handleLogout = () => {
    dispatch(unsetUserToken({ access_token: null }))
    dispatch(unsetUserInfo({ name: "", email: "" }))
    removeToken()
    navigate('/api/login')
  };

  React.useEffect(() => {
    if (data && isSuccess) {
      dispatch(setUserInfo({ email: data.email, name: data.name }))
    }
  }, [data, isSuccess, dispatch])

  return (
    <>
      <>
        {location.pathname === "/" ? <div className="wave-container"></div> : ""}
        <div>
          <Box sx={{ display: "flex" }}>
            <CssBaseline />
            <AppBar position="fixed" open={open}>
              <Toolbar>
                <IconButton
                  color="inherit"
                  aria-label="open drawer"
                  onClick={handleDrawerOpen}
                  edge="start"
                  sx={{
                    marginRight: 5,
                    ...(open && { display: "none" }),
                  }}
                >
                  <MenuIcon />
                </IconButton>
                <Typography variant="h6" noWrap component="div">
                  CerGen
                </Typography>
              </Toolbar>
              <div className="flex absolute top-20 right-2 hover:cursor-pointer hover:bg-blue-600 rounded-md text-white gap-3 bg-blue-500 shadow-lg shadow-sky-900 p-4">
                <PersonIcon />
                <p>{myData.name}</p>
              </div>
            </AppBar>
            <Drawer variant="permanent" open={open}>
              <DrawerHeader>
                <IconButton onClick={handleDrawerClose}>
                  {theme.direction === "rtl" ? (
                    <ChevronRightIcon />
                  ) : (
                    <ChevronLeftIcon />
                  )}
                </IconButton>
              </DrawerHeader>
              <Divider />
              <List>
                <Link to="/api/all-events">
                  <ListItem disablePadding sx={listitem_sx} key="all_events">
                    <ListItemButton sx={listItemButton_sx}>
                      <ListItemIcon sx={listItemIcon_sx}>
                        <EventIcon />
                      </ListItemIcon>
                      <ListItemText
                        primary="All Events"
                        sx={{ opacity: open ? 1 : 0 }}
                      />
                    </ListItemButton>
                  </ListItem>
                </Link>
              </List>
              <List>
                <div onClick={handleForm}>
                  <ListItem disablePadding sx={listitem_sx} key="create_events">
                    <ListItemButton sx={listItemButton_sx}>
                      <ListItemIcon sx={listItemIcon_sx}>
                        <AddCircleOutlineIcon />
                      </ListItemIcon>
                      <ListItemText
                        primary="Create Event"
                        sx={{ opacity: open ? 1 : 0 }}
                      />
                    </ListItemButton>
                  </ListItem>
                </div>
              </List>
              <List>
                <div onClick={handleCsvForm}>
                  <ListItem disablePadding sx={listitem_sx} key="upload_csv">
                    <ListItemButton sx={listItemButton_sx}>
                      <ListItemIcon sx={listItemIcon_sx}>
                        <FileUploadIcon />
                      </ListItemIcon>
                      <ListItemText
                        primary="Upload Participants"
                        sx={{ opacity: open ? 1 : 0 }}
                      />
                    </ListItemButton>
                  </ListItem>
                </div>
              </List>
              <Divider />
              <List>
                <Link to="/api/logout" onClick={handleLogout}>
                  <ListItem disablePadding sx={listitem_sx} key="logout">
                    <ListItemButton sx={listItemButton_sx}>
                      <ListItemIcon sx={listItemIcon_sx}>
                        <LogoutIcon />
                      </ListItemIcon>
                      <ListItemText
                        primary="Logout"
                        sx={{ opacity: open ? 1 : 0 }}
                      />
                    </ListItemButton>
                  </ListItem>
                </Link>
              </List>
            </Drawer>
            {location.pathname === "/" ? <Home /> : ""}
            <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
              <DrawerHeader />
            </Box>
            <EventForm open={form} onClose={handleFormClose} />
            <FileForm open={csv_form} onClose={handleCsvFormClose} />
          </Box>
          <BackdropSpinner open={openSpinner} />
        </div>
      </>
      <Footer />
    </>
  );
}
