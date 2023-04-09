import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const eventsAPI = createApi({
  reducerPath: "eventsAPI",
  baseQuery: fetchBaseQuery({ baseUrl: "http://127.0.0.1:8000/api/" }),
  endpoints: (builder) => ({
    getAllEvents: builder.query({
      query: (access_token) => {
        return {
          url: "all-events/",
          method: "GET",
          headers: {
            authorization: `Bearer ${access_token}`,
          },
        };
      },
    }),
    createEvent: builder.mutation({
      query: (data) => {
        return {
          url: "all-events/",
          method: "POST",
          body: data.eventData,
          headers: {
            "Content-type": "application/json; charset=UTF-8",
            authorization: `Bearer ${data.access_token}`,
          },
        };
      },
    }),
    deleteEvent: builder.mutation({
      query: (data) => {
        return {
          url: `event/${data.slug}`,
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
  useGetAllEventsQuery,
  useCreateEventMutation,
  useDeleteEventMutation,
} = eventsAPI;
