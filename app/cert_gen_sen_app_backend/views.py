from rest_framework.views import APIView
from django.http import JsonResponse
from .models import *
from .serializers import *
import pandas as pd

# Create your views here.

class AllEvents(APIView):
    def get(self, request):
        all_events = Event.objects.all()

        if all_events:
            event_serializer_data = EventSerializer(all_events,many=True)
            return JsonResponse(event_serializer_data.data,safe=False)
        return JsonResponse("No Data",safe=False)
    
class FilteredEvent(APIView):
    def get(self, request, slug):
        event = Event.objects.filter(slug=slug)

        if event:
            event_serializer = EventSerializer(event,many=True)
            return JsonResponse(event_serializer.data,safe=False)
        return JsonResponse("No Data",safe=False)

def generateCertificate(self,request):
    pass