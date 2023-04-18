import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const certificateGeneratorAPI = createApi({
  reducerPath: "certificateGeneratorAPI",
  baseQuery: fetchBaseQuery({ baseUrl: "http://127.0.0.1:8000/api/" }),
  endpoints: (builder) => ({
    getCompletionCertificate: builder.query({
      query: (access_token) => {
        console.log(access_token);
        return {
          url: "upload-completion-template",
          method: "GET",
          headers: {
            authorization: `Bearer ${access_token}`,
          },
        };
      },
    }),
    getContributeCompletionCertificate: builder.query({
      query: (access_token) => {
        return {
          url: "contribute-completion-template",
          method: "GET",
          headers: {
            authorization: `Bearer ${access_token}`,
          },
        };
      },
    }),
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
  useGetCompletionCertificateQuery,
  useGetContributeCompletionCertificateQuery,
  useGenerateCertificateByIdQuery,
  useGenerateCertificateQuery,
} = certificateGeneratorAPI;
