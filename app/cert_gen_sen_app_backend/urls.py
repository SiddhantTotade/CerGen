from .views import *
from django.urls import path

urlpatterns = [
    path("all-events/",EventsOperations.as_view()),
    path("event/<slug:slug>",FilteredEvent.as_view()),
    path("generate-certificate/",generateCertificate)
]