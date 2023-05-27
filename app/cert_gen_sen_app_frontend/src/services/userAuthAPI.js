import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const userAuthAPI = createApi({
  reducerPath: "userAuthAPI",
  baseQuery: fetchBaseQuery({ baseUrl: "http://127.0.0.1:8000/api/" }),
  endpoints: (builder) => ({
    registerUser: builder.mutation({
      query: (user) => {
        return {
          url: "register/",
          method: "POST",
          body: user,
          headers: {
            "Content-type": "application/json",
          },
        };
      },
    }),
    loginUser: builder.mutation({
      query: (user) => {
        return {
          url: "login/",
          method: "POST",
          body: user,
          headers: {
            "Content-type": "application/json",
          },
        };
      },
    }),
    getLoggedInUser: builder.query({
      query: (access_token) => {
        return {
          url: "profile/",
          method: "GET",
          headers: {
            authorization: `Bearer ${access_token}`,
          },
        };
      },
    }),
    changeUserPassword: builder.mutation({
      query: (data) => {
        const formData = new FormData();
        formData.append("password", data.password.new_password);
        formData.append("password2", data.password.confirm_new_password);
        return {
          url: "change-password/",
          method: "POST",
          body: formData,
          headers: {
            authorization: `Bearer ${data.access_token}`,
          },
        };
      },
    }),
    sendPasswordResetEmail: builder.mutation({
      query: (user) => {
        return {
          url: "reset-password/",
          method: "POST",
          body: user,
          headers: {
            "Content-type": "application/json",
          },
        };
      },
    }),
    resetPassword: builder.mutation({
      query: ({ actualData, id, token }) => {
        return {
          url: `reset-password/${id}/${token}/`,
          method: "POST",
          body: actualData,
          headers: {
            "Content-type": "application/json",
          },
        };
      },
    }),
    senderCredential: builder.mutation({
      query: (data) => {
        const formData = new FormData();
        formData.append("email", data.credential.email);
        formData.append("password", data.credential.password);
        formData.append("phone", data.phone);
        return {
          url: "sender-credential/",
          method: "POST",
          body: formData,
          headers: {
            authorization: `Bearer ${data.access_token}`,
          },
        };
      },
    }),
    getCredential: builder.query({
      query: (data) => {
        return {
          url: "sender-credential/",
          method: "GET",
          headers: {
            authorization: `Bearer ${data}`,
          },
        };
      },
    }),
  }),
});

export const {
  useRegisterUserMutation,
  useLoginUserMutation,
  useGetLoggedInUserQuery,
  useChangeUserPasswordMutation,
  useSendPasswordResetEmailMutation,
  useResetPasswordMutation,
  useGetCredentialQuery,
  useSenderCredentialMutation,
} = userAuthAPI;
