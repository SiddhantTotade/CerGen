import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const participantsAPI = createApi({
  reducerPath: "participantsAPI",
  baseQuery: fetchBaseQuery({ baseUrl: "http://127.0.0.1:8000/api/" }),
  endpoints: (builder) => ({
    getParticipants: builder.query({
      query: (data) => {
        return {
          url: `event/${data.event_slug}`,
          method: "GET",
          headers: {
            authorization: `Bearer ${data.access_token}`,
          },
        };
      },
    }),
    uploadParticipants: builder.mutation({
      query: (data) => {
        const formData = new FormData();
        formData.append(
          "participants_file",
          data.participantsFileData.participants_file
        );
        formData.append("event_id", data.participantsFileData.event_id);
        return {
          url: "upload-participants/",
          method: "POST",
          body: formData,
          headers: {
            authorization: `Bearer ${data.access_token}`,
          },
        };
      },
    }),
    createParticipant: builder.mutation({
      query: (data) => {
        return {
          url: "create-participant/",
          method: "POST",
          body: {
            event: data.event,
            participant_name: data.participant_data.participant_name,
            participant_id: data.participant_data.participant_id,
            email: data.participant_data.email,
            phone: data.phone,
            certificate_status: data.participant_data.certificate_status,
            certificate_id: data.certificate_id,
          },
          headers: {
            "Content-type": "application/json; charset=UTF-8",
            authorization: `Bearer ${data.access_token}`,
          },
        };
      },
    }),
    updateParticipant: builder.mutation({
      query: (data) => {
        return {
          url: `update-participant/${data.participant_data.id}`,
          method: "PUT",
          body: {
            event: data.event,
            participant_name: data.participant_data.participant_name,
            participant_id: data.participant_data.participant_id,
            email: data.participant_data.email,
            phone: data.phone,
            certificate_status: data.participant_data.certificate_status,
            certificate_id: data.certificate_id,
          },
          headers: {
            "Content-type": "application/json; charset=UTF-8",
            authorization: `Bearer ${data.access_token}`,
          },
        };
      },
    }),
    deleteParticipant: builder.mutation({
      query: (data) => {
        return {
          url: `delete-participant/${data.participant_data.id}`,
          method: "DELETE",
          headers: {
            authorization: `Bearer ${data.access_token}`,
          },
        };
      },
    }),
  }),
});

export const {
  useGetParticipantsQuery,
  useUploadParticipantsMutation,
  useCreateParticipantMutation,
  useUpdateParticipantMutation,
  useDeleteParticipantMutation,
} = participantsAPI;
