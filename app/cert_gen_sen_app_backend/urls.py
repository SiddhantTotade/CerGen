from .views import *
from django.urls import re_path,path

urlpatterns = [
    re_path(r"^all-events",AllEvents.as_view()),
    path("event/<slug:slug>",FilteredEvent.as_view())
]