from .views import *
from django.urls import path
from .certificate_generator import *

urlpatterns = [
    path("all-events/",EventsOperations.as_view()),
    path("event/<slug:slug>",FilteredEvent.as_view()),
    path("event-details/<slug:slug>",get_event_by_slug),
    path("create-participant/",UploadEachParticipant.as_view()),
    path("update-participant/<int:pk>",UploadEachParticipant.as_view()),
    path("delete-participant/<int:pk>",UploadParticipant.as_view()),
    path("upload-participants/",UploadParticipant.as_view()),
    path("generate-certificate/<slug:slug>",generateCertificate),
]