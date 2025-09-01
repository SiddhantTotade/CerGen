import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    access_token: 0
}

export const authSlice = createSlice({
    name: 'auth_token',
    initialState,
    reducers: {
        setUserToken: (state, action) => {
            state.access_token = action.payload.access_token
        },
        unsetUserToken: (state, action) => {
            state.access_token = action.payload.access_token
        }
    }
})

export const { setUserToken, unsetUserToken } = authSlice.actions

export default authSlice.reducer