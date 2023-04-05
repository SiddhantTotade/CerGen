import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const eventsAPI = createApi({
  reducerPath: "eventsAPI",
  baseQuery: fetchBaseQuery({ baseUrl: "http://127.0.0.1:8000/api/" }),
  endpoints: (builder) => ({
    getAllEvents: builder.query({
      query: (access_token) => {
        return {
          url: "all-events/",
          method: "POST",
          headers: {
            authorization: `Bearer ${access_token}`,
          },
        };
      },
    }),
  }),
});

export const { useGetAllEventsQuery } = eventsAPI;
