import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const certificateGeneratorAPI = createApi({
  reducerPath: "certificateGeneratorAPI",
  baseQuery: fetchBaseQuery({ baseUrl: "http://127.0.0.1:8000/api/" }),
  endpoints: (builder) => ({
    getCompletionCertificate: builder.query({
      query: (access_token) => {
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
    getMeritCertificate: builder.query({
      query: (access_token) => {
        return {
          url: "upload-merit-template",
          method: "GET",
          headers: {
            authorization: `Bearer ${access_token}`,
          },
        };
      },
    }),
    getContributeMeritCertificate: builder.query({
      query: (access_token) => {
        return {
          url: "contribute-merit-template",
          method: "GET",
          headers: {
            authorization: `Bearer ${access_token}`,
          },
        };
      },
    }),
    previewTemplate: builder.mutation({
      query: (data) => {
        const formData = new FormData();
        formData.append("pptx_file", data.previewFile);
        return {
          url: "preview-certificate/",
          method: "POST",
          body: formData,
          headers: {
            authorization: `Bearer ${data.access_token}`,
          },
        };
      },
    }),
    uploadCompletionTemplate: builder.mutation({
      query: (data) => {
        const formData = new FormData();
        formData.append("pptx_file", data.pptx_file);
        formData.append("contribute", data.contribute);
        return {
          url: "upload-completion-template/",
          method: "POST",
          body: formData,
          headers: {
            authorization: `Bearer ${data.access_token}`,
          },
        };
      },
    }),
    uploadMeritTemplate: builder.mutation({
      query: (data) => {
        const formData = new FormData();
        formData.append("pptx_file", data.pptx_file);
        formData.append("contribute", data.contribute);
        return {
          url: "upload-merit-template/",
          method: "POST",
          body: formData,
          headers: {
            authorization: `Bearer ${data.access_token}`,
          },
        };
      },
    }),
    generateCertificate: builder.mutation({
      query: (data) => {
        return {
          url: `generate-certificate/${data.event_slug}`,
          method: "POST",
          body: {
            completion: data.completion.replace("jpg", "pptx"),
            merit: data.merit.replace("jpg", "pptx"),
          },
          headers: {
            authorization: `Bearer ${data.access_token}`,
          },
        };
      },
    }),
    generateCertificateById: builder.mutation({
      query: (data) => {
        return {
          url: `generate-certificate/${data.event_slug}/${data.id}`,
          method: "POST",
          body: {
            completion: data.completion.replace("jpg", "pptx"),
            merit: data.merit.replace("jpg", "pptx"),
          },
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
  useGetMeritCertificateQuery,
  useGetContributeMeritCertificateQuery,
  usePreviewTemplateMutation,
  useUploadCompletionTemplateMutation,
  useUploadMeritTemplateMutation,
  useGenerateCertificateMutation,
  useGenerateCertificateByIdMutation,
} = certificateGeneratorAPI;
