import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const participantsImagesAPI = createApi({
  reducerPath: "participantsImageAPI",
  baseQuery: fetchBaseQuery({ baseUrl: "http://127.0.0.1:8000/api/" }),
  endpoints: (builder) => ({
    getParticipantImage: builder.query({
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
    uploadParticipantImage: builder.mutation({
      query: (data) => {
        const formData = new FormData();
        formData.append("participant_image", data.imgSrc);
        return {
          url: `upload-participant-image/${data.event}`,
          method: "PATCH",
          body: formData,
          headers: {
            authorization: `Bearer ${data.access_token}`,
          },
        };
      },
    }),
    getAlbumImages: builder.query({
      query: (data) => {
        return {
          url: "create-participant/",
          method: "GET",
          body: "",
          headers: {
            "Content-type": "application/json; charset=UTF-8",
            authorization: `Bearer ${data.access_token}`,
          },
        };
      },
    }),
    UploadAlbumImages: builder.mutation({
      query: (data) => {
        const formData = new FormData();
        formData.append("event", data.event_slug);
        data.album.forEach((img) => {
          formData.append("album_images", img);
        });
        return {
          url: `upload-event-album/${data.event_slug}`,
          method: "POST",
          body: formData,
          headers: {
            authorization: `Bearer ${data.access_token}`,
          },
        };
      },
    }),
  }),
});

export const {
  useGetParticipantImageQuery,
  useUploadParticipantImageMutation,
  useGetAlbumImagesQuery,
  useUploadAlbumImagesMutation,
} = participantsImagesAPI;
