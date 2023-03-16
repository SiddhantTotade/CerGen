from rest_framework.views import APIView
from django.http import JsonResponse
from .models import *
from .serializers import *
from .resources import *
import openpyxl
from itertools import islice
from collections import OrderedDict
from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.viewsets import ModelViewSet
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.conf import settings
import random
import os
import string
# Create your views here.


# Getting single events by slug
@permission_classes((IsAuthenticated,))
def get_event_by_slug(request, slug):
    event = Event.objects.filter(slug=slug)
    if event:
        event_data = EventSerializer(event, many=True)
        return JsonResponse(event_data.data, safe=False)
    return JsonResponse("No Data", safe=False)


# Generating UID
def generate_uid(stu_id, eve_name, eve_dept, eve_date):
    random_num = random.randint(1000, 9999)
    certificate_id = str(stu_id)+str(eve_name)+str(eve_dept) + \
        str(eve_date).replace("-", "")+str(random_num)
    return certificate_id


# ManageUser API
class ManageUserAPI(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# Getting all events
@permission_classes((IsAuthenticated,))
class EventsOperations(APIView):
    def get(self, request):
        all_events = reversed(Event.objects.all())

        if all_events:
            event_serializer_data = EventSerializer(all_events, many=True)
            return JsonResponse(event_serializer_data.data, safe=False)
        return JsonResponse("No event data", safe=False)

    def post(self, request):
        event_serialized_data = EventSerializer(data=request.data)

        if event_serialized_data.is_valid():
            event_serialized_data.save()
            return JsonResponse("Event added successfully", safe=False)
        return JsonResponse("Failed to add event", safe=False)


# Getting data from xlsx and uploading to database
class UploadParticipant(APIView):
    def get(self, request):
        all_participants = Participant.objects.all()

        if all_participants:
            participant_serializer = ParticipantSerializer(
                all_participants, many=True)
            return JsonResponse(participant_serializer.data, safe=False)
        return JsonResponse("No participant data", safe=False)

    def post(self, request):
        event_id = request.data['eventId']
        participant_file = request.data['xlsx_file']

        wb = openpyxl.load_workbook(participant_file)
        work_sheet = wb['Form Responses 1']

        excel_data = list()
        for row in islice(work_sheet.values, 1, work_sheet.max_row):
            data = OrderedDict()
            data['id'] = row[0]
            data['Full_Name'] = row[1]
            data['Student_Id'] = row[2]
            data['Email'] = row[3]
            data['Certificate_Status'] = row[4]
            excel_data.append(data)

        eve_id = Event.objects.filter(id=event_id)
        event_new_id = Event.objects.get(id=event_id)

        event_name = ''
        event_dept = ''
        event_date = ''

        for eve in eve_id:
            event_name = eve.event_name
            event_dept = eve.event_department
            event_date = eve.from_date

        event_name_words = event_name.split()
        event_name_chars_list = [word[0] for word in event_name_words]
        event_name_chars_string = "".join(event_name_chars_list)

        for data in excel_data:
            name = data['Full_Name']
            student_id = data['Student_Id']
            email = data['Email']
            certificate_status = data['Certificate_Status']
            certificate_id = generate_uid(data['Student_Id'], event_name_chars_string,
                                          event_dept, event_date)
            Event.id = Participant.objects.create(
                event=event_new_id, student_name=name, student_id=student_id, email=email, certificate_status=certificate_status, certificate_id=certificate_id)

        return JsonResponse("Participants uploaded successfully", safe=False)

    def delete(self, request, pk):
        participant_by_slug = Participant.objects.get(pk=pk)
        participant_by_slug.delete()
        return JsonResponse("Participant deleted successfully", safe=False)


# Uploading each participant from xlsx file
class UploadEachParticipant(APIView):
    def post(self, request):
        participant_serialized_data = ParticipantSerializer(data=request.data)

        if participant_serialized_data.is_valid():
            participant_serialized_data.save()
            return JsonResponse("Participant added successfully", safe=False)
        return JsonResponse("Failed to add participant", safe=False)

    def put(self, request, pk):
        participant_json_data = JSONParser().parse(request)
        participant_by_id = Participant.objects.get(pk=pk)
        participant_serialized_data = ParticipantSerializer(
            participant_by_id, data=participant_json_data)

        if participant_serialized_data.is_valid():
            participant_serialized_data.save()
            return JsonResponse("Participant updated successfully", safe=False)
        return JsonResponse("Failed to update participant", safe=False)


# Filtering Events by slug
@ permission_classes((IsAuthenticated,))
class FilteredEvent(APIView):
    def get(self, request, slug):
        event = Event.objects.filter(slug=slug)
        event_date = ""
        event_department = ""
        new_event_id = 0
        for event_id in event:
            new_event_id = event_id
            event_date = event_id.from_date
            event_department = event_id.event_department
        participants = reversed(Participant.objects.filter(event=new_event_id))

        if participants:
            participants = ParticipantSerializer(participants, many=True)
            return Response({'participants_data': participants.data, 'event_date': event_date, 'event_department': event_department})
        return JsonResponse("0", safe=False)

    def delete(self, request, slug):
        event_by_slug = Event.objects.get(slug=slug)
        event_by_slug.delete()
        return JsonResponse("Event deleted successfully", safe=False)


class UploadCompletionTemplate(ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        # pptx_file_serializer = CompletionCertificateSerializer(
        #     data=request.data)

        # print(request.data)

        # if pptx_file_serializer.is_valid():
        #     pptx_file_serializer.save()

        file = request.FILES['pptx_file']
        user = request.user.id
        user_id = User.objects.get(id=user)
        CompletionCertificateTemplate.objects.create(
            user=user_id, template=file).save()

        # letters_and_digits = string.ascii_letters + string.digits
        # file_name_str = "".join(random.choice(
        #     letters_and_digits)for i in range(15))

        # completion_certificate = request.FILES['pptx_file']

        # file_name = file_name_str + completion_certificate.name

        # img_file_name = os.path.splitext(file_name)[0]

        # file_path = os.path.join(
        #     settings.BASE_DIR, './cert_gen_sen_app_backend/certificate_data/upload-ppt-file/', file_name)

        # with open(file_path, 'wb+') as destination:
        #     for chunk in completion_certificate.chunks():
        #         destination.write(chunk)

        # ppt_to_image_command = f'unoconv -f jpg ./cert_gen_sen_app_backend/certificate_data/upload-ppt-file/{file_name}'
        # os.system(ppt_to_image_command)

        # file_upload = CompletionCertificateTemplate.objects.create(
        #     user=user_id, template=f'./cert_gen_sen_app_backend/certificate_data/upload-ppt-file/{file_name}', template_img=f'./cert_gen_sen_app_backend/certificate_data/upload-ppt-file/{img_file_name}.jpg')
        # file_upload.save()

        return JsonResponse("Template uploaded successfully", safe=False)
