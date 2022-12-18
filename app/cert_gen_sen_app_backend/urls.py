from .views import *
from django.urls import path

urlpatterns = [
    path("all-events/",EventsOperations.as_view()),
    path("event/<slug:slug>",FilteredEvent.as_view()),
    path("event-details/<slug:slug>",get_event_by_slug),
    path("create-participant/",UploadEachParticipant.as_view()),
    path("update-participant/<int:pk>",UpdateEachParticipant.as_view()),
    path("generate-certificate/",generateCertificate),
    path("upload-participants/",UploadParticipant.as_view()),
]