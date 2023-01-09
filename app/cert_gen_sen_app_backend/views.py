from rest_framework.views import APIView
from django.http import JsonResponse
from .models import *
from .serializers import *
import pandas as pd
from .resources import *
import openpyxl
from itertools import islice
from collections import OrderedDict
from rest_framework.parsers import JSONParser
# Create your views here.

# Getting all events
class EventsOperations(APIView):
    def get(self, request):
        all_events = Event.objects.all()

        if all_events:
            event_serializer_data = EventSerializer(all_events,many=True)
            return JsonResponse(event_serializer_data.data,safe=False)
        return JsonResponse("No event data",safe=False)
    
    def post(self, request):
        event_serialized_data = EventSerializer(data=request.data)

        if event_serialized_data.is_valid():
            event_serialized_data.save()
            return JsonResponse("Event added successfully",safe=False)
        return JsonResponse("Failed to add event",safe=False)


# Getting data from xlsx and uploading to database
class UploadParticipant(APIView):
    def get(self, request):
        all_participants = Participant.objects.all()

        if all_participants:
            participant_serializer = ParticipantSerializer(all_participants,many=True)
            return JsonResponse(participant_serializer.data,safe=False)
        return JsonResponse("No participant data",safe=False)

    def post(self, request):
        event_id = request.data['eventId']
        participant_file = request.data['xlsx_file']

        wb = openpyxl.load_workbook(participant_file)
        work_sheet = wb['Form Responses 1']

        excel_data = list()
        for row in islice(work_sheet.values,1,work_sheet.max_row):
            data = OrderedDict()
            data['id'] = row[0]
            data['First_Name'] = row[1]
            data['Email'] = row[2]
            data['Certificate_Status'] = row[3]
            excel_data.append(data)

        event_new_id = Event.objects.get(id = event_id)
        
        for data in excel_data:
            name = data['First_Name']
            email = data['Email']
            certificate_status = data['Certificate_Status']
            Event.id = Participant.objects.create(event = event_new_id,student_name = name,email = email, certificate_status = certificate_status)
        return JsonResponse("Participant uploaded successfully",safe=False)
    
    def delete(self, request, pk):
        participant_by_slug = Participant.objects.get(pk = pk)
        participant_by_slug.delete()
        return JsonResponse("Participant deleted successfully",safe=False)

# Getting single events by slug
def get_event_by_slug(request,slug):
    event = Event.objects.filter(slug=slug)
    if event:
        event_data = EventSerializer(event,many=True)
        return JsonResponse(event_data.data,safe= False)
    return JsonResponse("No Data",safe=False)

# Uploading each participant from xlsx file
class UploadEachParticipant(APIView):
    def post(self, request):
        participant_serialized_data = ParticipantSerializer(data=request.data)

        if participant_serialized_data.is_valid():
            participant_serialized_data.save()
            return JsonResponse("Participant added successfully",safe=False)
        return JsonResponse("Failed to add participant",safe=False)
    
    def put(self, request, pk):
        participant_json_data = JSONParser().parse(request)
        participant_by_id = Participant.objects.get(pk = pk)
        participant_serialized_data = ParticipantSerializer(participant_by_id,data=participant_json_data)

        if participant_serialized_data.is_valid():
            participant_serialized_data.save()
            return JsonResponse("Participant updated successfully",safe=False)
        return JsonResponse("Failed to update participant",safe=False)

# Filtering Events by slug
class FilteredEvent(APIView):
    def get(self, request, slug):
        event = Event.objects.filter(slug=slug)
        new_event_id = 0
        for event_id in event:
            new_event_id = event_id
        participants = Participant.objects.filter(event=new_event_id)

        if participants:
            participants = ParticipantSerializer(participants,many=True)
            return JsonResponse(participants.data,safe=False)
        return JsonResponse("0",safe=False)

    def delete(self, request, slug):
        event_by_slug = Event.objects.get(slug = slug)
        event_by_slug.delete()
        return JsonResponse("Event deleted successfully",safe=False)