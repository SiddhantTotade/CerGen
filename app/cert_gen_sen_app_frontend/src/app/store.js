import { configureStore } from "@reduxjs/toolkit";
import { setupListeners } from "@reduxjs/toolkit/query";
import { userAuthAPI } from "../services/userAuthAPI";
import authSlice from "../features/authSlice";
import userSlice from "../features/userSlice";
import { eventsAPI } from "../services/eventsAPI";
import { participantsAPI } from "../services/participantsAPI";

export const store = configureStore({
  reducer: {
    [userAuthAPI.reducerPath]: userAuthAPI.reducer,
    [eventsAPI.reducerPath]: eventsAPI.reducer,
    [participantsAPI.reducerPath]: participantsAPI.reducer,
    auth: authSlice,
    user: userSlice,
  },

  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(
      userAuthAPI.middleware,
      eventsAPI.middleware,
      participantsAPI.middleware
    ),
});

setupListeners(store.dispatch);
