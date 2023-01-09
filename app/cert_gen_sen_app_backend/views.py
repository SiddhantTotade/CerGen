from rest_framework.views import APIView
from django.http import JsonResponse
from .models import *
from .serializers import *
import pandas as pd
import glob
import os
import cv2
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

    
# Certificate directory cleaner
def cleanUp():
    participant_files = "../app/cert_gen_sen_app_backend/certificate_data/participants-certificates"
    participant_filelist = glob.glob(os.path.join(participant_files, "*"))
    for f in participant_filelist:
        os.remove(f)
        
    merit_files = "../app/cert_gen_sen_app_backend/certificate_data/merit-certificates"
    merit_filelist = glob.glob(os.path.join(merit_files, "*"))
    for f in merit_filelist:
        os.remove(f)

def meritCertificateGenerate(name, rank, event, from_date, to_date, template, signature, count):
    x_offset = 652
    y_offset = 1170

    y1, y2 = y_offset, y_offset + signature.shape[0]
    x1, x2 = x_offset, x_offset + signature.shape[1]

    alpha_s = signature[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        template[y1:y2, x1:x2, c] = (
            alpha_s * signature[:, :, c] + alpha_l * template[y1:y2, x1:x2, c])

    cv2.putText(template, name, (676, 632), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 4, (255, 0, 30), 3, cv2.LINE_AA)
    cv2.putText(template, rank, (1048, 748), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 0, 30), 2, cv2.LINE_AA)
    cv2.putText(template, event, (812, 838), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 0, 30), 2, cv2.LINE_AA)
    # cv2.putText(template, year, (1210, 1034), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 0, 30), 2, cv2.LINE_AA)
    if from_date == to_date:
        cv2.putText(template, from_date, (872, 938), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
    else:
        cv2.putText(template, from_date, (732, 914), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
        cv2.putText(template, to_date, (782, 552), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.imwrite(f'./cert_gen_sen_app_backend/certificate_data/merit-certificates/{str(count)+" "+name}.jpg', template)
    count += 1

        
# Ceertificate generator
def generateCertificate(request,slug):
    cleanUp()

    event = Event.objects.filter(slug=slug)
    event_list = []
    for eve in event:
        event_list.append(eve.event_name)
        event_list.append(str(eve.from_date))
        event_list.append(str(eve.to_date))
    
    event_date_check = False
    if event_list[1] == event_list[2]:
        event_date_check = True

    new_event_id = 0
    for event_id in event:
        new_event_id = event_id
    participants = Participant.objects.filter(event=new_event_id)
    participant_list = []
    for participant in participants:
        participant_list.append([participant.student_name,participant.email,participant.certificate_status])
    
    count = 1
    
    for data in participant_list:
        signature = cv2.imread("./cert_gen_sen_app_backend/certificate_data/certificate-generator/Galvin Belson.png", -1)
        template_base_dir = "./cert_gen_sen_app_backend/certificate_data/certificate-generator/"
        if data[2] == "1" or data[2] == "2" or data[2] == "3":
            if data[2] == "1":
                template = cv2.imread(template_base_dir + "certificate_1st.jpg")
                meritCertificateGenerate(data[0],data[2]+"st",event_list[0],event_list[1],event_list[2],template,signature,count)
            elif data[2] == "2":
                template = cv2.imread(template_base_dir + "certificate_2nd.jpg")
                meritCertificateGenerate(data[0],data[2]+"nd",event_list[0],event_list[1],event_list[2],template,signature,count)
            elif data[2] == "3":
                template = cv2.imread(template_base_dir + "certificate_3rd.jpg")
                meritCertificateGenerate(data[0],data[2]+"rd",event_list[0],event_list[1],event_list[2],template,signature,count)
        else:
            template = cv2.imread(template_base_dir + "certificate_of_completion.jpg")
            x_offset = 578
            y_offset = 1020

            y1, y2 = y_offset, y_offset + signature.shape[0]
            x1, x2 = x_offset, x_offset + signature.shape[1]

            alpha_s = signature[:, :, 3] / 255.0
            alpha_l = 1.0 - alpha_s

            for c in range(0, 3):
                template[y1:y2, x1:x2, c] = (
                    alpha_s * signature[:, :, c] + alpha_l * template[y1:y2, x1:x2, c])

            cv2.putText(template, data[0], (592, 704), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 4, (255, 0, 30), 3, cv2.LINE_AA)
            cv2.putText(template, event_list[0], (1036, 838), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 0, 30), 2, cv2.LINE_AA)
            if event_date_check:
                cv2.putText(template, event_list[1], (730, 886), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
            else:
                cv2.putText(template, event_list[1], (732, 914), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 30), 2, cv2.LINE_AA)
                # cv2.putText(template, event_list[2], (782, 552), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.imwrite(f'./cert_gen_sen_app_backend/certificate_data/participants-certificates/{str(count)+" "+data[0]}.jpg', template)
            count += 1
        # print(f'Processing {index + 1} / {len(key)}')
    return JsonResponse("Certificate Generated",safe=False)