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
    createEvent: builder.mutation(() => ({
      query: (data, access_token) => {
        return {
          url: "all-events/",
          body: data,
          method: "POST",
          user: "",
          headers: {
            "Content-type": "application/json,charset=utf-8",
            authorization: `Bearer ${access_token}`,
          },
        };
      },
    })),
  }),
});

export const { useGetAllEventsQuery } = eventsAPI;
