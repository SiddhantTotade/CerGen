import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const participantsAPI = createApi({
  reducerPath: "certificateGeneratorAPI",
  baseQuery: fetchBaseQuery({ baseUrl: "http://127.0.0.1:8000/api/" }),
  endpoints: (builder) => ({
    generateCertificate: builder.query({
      query: (data) => {
        return {
          url: `generate-certificate/${data.event_slug}`,
          method: "POST",
          headers: {
            authorization: `Bearer ${data.access_token}`,
          },
        };
      },
    }),
    generateCertificateById: builder.query({
      query: (data) => {
        return {
          url: `generate-certificate/${data.event_slug}/${data.id}`,
          method: "POST",
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
