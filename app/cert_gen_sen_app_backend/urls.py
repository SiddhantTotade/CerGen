from .views import *
from django.urls import path
from .certificate_generator import *
from .ppt_2_image_preview import *

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change-password/', UserChangePasswordView.as_view(),
         name='change_password'),
    path('reset-password/', SendPasswordResetEmailView.as_view(),
         name='send_reset_email_password'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(),
         name='reset_password'),

    path('sender-credential/', SenderCredentialView.as_view()),
    path("all-events/", EventsView.as_view()),
    path("all-events/<int:pk>", EventsView.as_view()),
    path("event/<slug:slug>", FilteredEventView.as_view()),
    path("event-details/<slug:slug>", get_event_by_slug),
    path("create-participant/", UploadEachParticipantView.as_view()),
    path("update-participant/<int:pk>", UploadEachParticipantView.as_view()),
    path("delete-participant/<int:pk>", UploadParticipantView.as_view()),
    path("upload-participants/", UploadParticipantView.as_view()),
    path("upload-participant-image/<int:pk>",
         UploadParticipantImageView.as_view()),
    path("upload-event-album/<slug:slug>",
         ParticipantImageAlbumView.as_view()),
    path("generate-certificate/<slug:slug>", GenerateCertificate.as_view()),
    path("generate-certificate/<slug:slug>/<int:pk>",
         GenerateCertificateById.as_view()),
    path("preview-certificate/", Ppt2Image.as_view()),
    path("upload-completion-template/",
         UploadCompletionTemplateView.as_view()),
    path("upload-merit-template/",
         UploadMeritTemplateView.as_view()),
    path("contribute-completion-template/",
         ContributeCompletionView.as_view()),
    path("contribute-merit-template/",
         ContributeMeritView.as_view()),
]
