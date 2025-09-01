import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    access_token: 0
}

export const authSlice = createSlice({
    name: 'user_info',
    initialState,
    reducers: {
        setUserInfo: (state, action) => {
            state.email = action.payload.email
            state.name = action.payload.name
        },
        unsetUserInfo: (state, action) => {
            state.email = action.payload.email
            state.name = action.payload.name
        },
    }
})

export const { setUserInfo, unsetUserInfo } = authSlice.actions

export default authSlice.reducer