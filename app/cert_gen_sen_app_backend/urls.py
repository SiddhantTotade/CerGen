from .views import *
from django.urls import path
from .certificate_generator import *
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI
from .ppt_2_image_preview import *

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('profile/', ManageUserAPI.as_view(), name='manage_user'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutal'),

    path("all-events/", EventsOperations.as_view()),
    path("event/<slug:slug>", FilteredEvent.as_view()),
    path("event-details/<slug:slug>", get_event_by_slug),
    path("create-participant/", UploadEachParticipant.as_view()),
    path("update-participant/<int:pk>", UploadEachParticipant.as_view()),
    path("delete-participant/<int:pk>", UploadParticipant.as_view()),
    path("upload-participants/", UploadParticipant.as_view()),
    path("generate-certificate/<slug:slug>", GenerateCertificate.as_view()),
    path("generate-certificate/<slug:slug>/<int:pk>", generate_certificate_by_id),
    path("preview-certificate/", Ppt2Image.as_view()),
    path("upload-completion-template/",
         UploadCompletionTemplate.as_view()),
    path("upload-merit-template/",
         UploadMeritTemplate.as_view()),
    path("contribute-merit-template/",
         ContributeMerit.as_view()),
    path("contribute-completion-template/",
         ContributeCompletion.as_view()),
]
