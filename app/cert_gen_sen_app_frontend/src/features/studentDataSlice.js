import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  access_token: 0,
};

export const participantDataSlice = createSlice({
  name: "student_data",
  initialState,
  reducers: {
    setParticipantData: (state, action) => {
      state.id = action.payload.id;
      state.event = action.payload.event;
      state.participant_name = action.payload.participant_name;
      state.participant_id = action.payload.participant_id;
      state.email = action.payload.email;
      state.phone = action.payload.phone;
      state.certificate_status = action.payload.certificate_status;
      state.certificate_id = action.payload.certificate_id;
      state.certificate_sent_status = action.payload.certificate_sent_status;
      state.student_image = action.payload.student_image;
    },
    unsetParticipantData: (state, action) => {
      state.id = action.payload.id;
      state.event = action.payload.event;
      state.participant_name = action.payload.participant_name;
      state.participant_id = action.payload.participant_id;
      state.email = action.payload.email;
      state.phone = action.payload.phone;
      state.certificate_status = action.payload.certificate_status;
      state.certificate_id = action.payload.certificate_id;
      state.certificate_sent_status = action.payload.certificate_sent_status;
      state.student_image = action.payload.student_image;
    },
  },
});

export const { setParticipantData, unsetParticipantData } =
  participantDataSlice.actions;

export default participantDataSlice.reducer;
