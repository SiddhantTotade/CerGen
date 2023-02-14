import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

export const userAuthAPI = createApi({
    reducerPath: 'userAuthAPI',
    baseQuery: fetchBaseQuery({ baseUrl: 'http://127.0.0.1:8000/api/user' })
})