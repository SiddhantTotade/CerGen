import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  access_token: 0,
};

export const eventsSlice = createSlice({
  name: "user_info",
  initialState,
  reducers: {
    setEventInfo: (state, action) => {
      state.email = action.payload.email;
      state.name = action.payload.name;
    },
    unsetEventInfo: (state, action) => {
      state.email = action.payload.email;
      state.name = action.payload.name;
    },
  },
});

export const { setUserInfo, unsetUserInfo } = eventsSlice.actions;

export default eventsSlice.reducer;
