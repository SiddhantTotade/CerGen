from django.urls import path

from .views import registration, login, profile, logout

urlpatterns = [
    path("register/", registration.UserRegistrationView.as_view(), name="register"),
    path("login/", login.UserLoginView.as_view(), name="login"),
    path("profile/", profile.UserProfile.as_view(), name="profile"),
    path("logout/", logout.UserLogoutView.as_view(), name="logout"),
    # path(
    #     "generate-key/",
    #     registrationKey.GenerateKeyView.as_view(),
    #     name="registrationKey",
    # ),
]