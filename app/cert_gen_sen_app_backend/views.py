from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import *
from .models import *
from .serializers import *
from .resources import *
from .helpers import *
from itertools import islice
from collections import OrderedDict
import openpyxl
import random


# Create your views here.

# Generate access and refresh tokens for users
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


# User registration view
class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token': token, 'msg': 'Admin registered successfully'}, status=status.HTTP_201_CREATED)


# User login view
class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token': token, 'msg': 'Login success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'non_fields_errors': ['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)


# User profile view
class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# User change password view
class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(
            data=request.data, context={'user': request.user})

        serializer.is_valid(raise_exception=True)
        return Response({'data': 'Password changed successfully'}, status=status.HTTP_200_OK)


# User send password-reset link view
class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserSendPasswordResetEmailSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password reset link has been sent on your e-mail'}, status=status.HTTP_200_OK)


# User password-reset view
class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(
            data=request.data, context={'uid': uid, 'token': token})

        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password reset successfully'}, status=status.HTTP_200_OK)


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


class SenderCredentialView(APIView):
    def get(self, request):
        try:
            user_id = request.user.id

            if SendersCredentials.objects.filter(user=user_id).exists():
                return JsonResponse("Something went wrong", safe=False)
        except:
            return JsonResponse("Something went wrong", safe=False)

    def post(self, request):
        try:
            user_id = request.user.id
            user = User.objects.get(id=user_id)

            if SendersCredentials.objects.filter(user=user_id).exists():
                SendersCredentials.objects.update(
                    user=user, senders_email=request.data['email'], senders_password=request.data['password'], senders_phone=request.data['phone'])
            else:
                SendersCredentials.objects.create(
                    user=user, senders_email=request.data['email'], senders_password=request.data['password'], senders_phone=request.data['phone'])

            return JsonResponse("Sender credentials saved successfully", safe=False)
        except:
            return JsonResponse("Failed to save credentials", safe=False)


# Getting all events view
class EventsView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_events = Event.objects.filter(user=request.user)

        if all_events:
            event_serializer_data = EventSerializer(
                all_events, many=True)
            return JsonResponse(event_serializer_data.data, safe=False)
        return JsonResponse("No event data", safe=False)

    def post(self, request):
        event_serialized_data = EventSerializer(data=request.data)

        if event_serialized_data.is_valid():
            event_serialized_data.save()
            return JsonResponse("Event added successfully", safe=False)
        return JsonResponse("Failed to add event", safe=False)

    def put(self, request, pk):
        event_id = Event.objects.get(id=pk)
        event_serialized_data = EventSerializer(
            instance=event_id, data=request.data, partial=True)

        if event_serialized_data.is_valid():
            event_serialized_data.save()
            return JsonResponse("Event updated successfully", safe=False)
        return JsonResponse("Failed to update event", safe=False)


# Getting data from xlsx and uploading to database
class UploadParticipantView(APIView):
    def get(self, request):
        all_participants = Participant.objects.all()

        if all_participants:
            participant_serializer = ParticipantSerializer(
                all_participants, many=True)
            return JsonResponse(participant_serializer.data, safe=False)
        return JsonResponse("No participant data", safe=False)

    def post(self, request):
        try:
            event_id = request.data['event_id']
            participant_file = request.data['participants_file']

            wb = openpyxl.load_workbook(participant_file)
            work_sheet = wb['Form Responses 1']

            excel_data = list()
            for row in islice(work_sheet.values, 1, work_sheet.max_row):
                data = OrderedDict()
                data['id'] = row[0]
                data['Full_Name'] = row[1]
                data['Participant_Id'] = row[2]
                data['Email'] = row[3]
                data['Phone'] = row[4]
                data['Certificate_Status'] = row[5]
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

            participants_list = []

            for data in excel_data:
                participant_name = data['Full_Name']
                participant_id = data['Participant_Id']
                email = data['Email']
                phone = data['Phone']
                if "+91" in str(phone):
                    phone = data['Phone']
                else:
                    phone = "+91"+str(data['Phone'])
                certificate_status = data['Certificate_Status']
                certificate_id = generate_uid(data['Participant_Id'], event_name_chars_string,
                                              event_dept, event_date)
                participants_list.append(Participant(event=event_new_id, participant_name=participant_name, participant_id=participant_id,
                                         email=email, phone=phone, certificate_status=certificate_status, certificate_id=certificate_id))

            Event.id = Participant.objects.bulk_create(participants_list)

            return JsonResponse("Participants uploaded successfully", safe=False)
        except:
            return JsonResponse("Failed to upload participants", safe=False)

    def delete(self, request, pk):
        try:
            participant_by_slug = Participant.objects.get(pk=pk)
            participant_by_slug.delete()
            return JsonResponse("Participant deleted successfully", safe=False)
        except:
            return JsonResponse("Failed to delete participants", safe=False)


# Uploading each participant from xlsx file
class UploadEachParticipantView(APIView):
    def post(self, request):
        participant_serialized_data = ParticipantSerializer(data=request.data)

        if participant_serialized_data.is_valid():
            participant_serialized_data.save()
            return JsonResponse("Participant added successfully", safe=False)
        return JsonResponse("Failed to add participant", safe=False)

    def put(self, request, pk):
        participant_by_id = Participant.objects.get(pk=pk)
        participant_serialized_data = ParticipantSerializer(
            instance=participant_by_id, data=request.data, partial=True)

        if participant_serialized_data.is_valid():
            participant_serialized_data.save()
            return JsonResponse("Participant updated successfully", safe=False)
        return JsonResponse("Failed to update participant", safe=False)


# Upload participant image
class UploadParticipantImageView(APIView):
    def patch(self, request, pk):
        try:
            participant_img = request.FILES['participant_image']
            image = Participant.objects.get(id=pk)
            image.participant_image = participant_img
            image.save()

            return JsonResponse("Image uploaded successfully", safe=False)
        except:
            return JsonResponse("Failed to uploaded image", safe=False)


# Filtering events by slug
@ permission_classes((IsAuthenticated,))
class FilteredEventView(APIView):
    def get(self, request, slug):
        event = Event.objects.get(slug=slug)
        participants = reversed(Participant.objects.filter(event=event))

        if participants:
            participants = ParticipantSerializer(participants, many=True)
            return JsonResponse(participants.data, safe=False)
        return JsonResponse("0", safe=False)

    def delete(self, request, slug):
        try:
            event_by_slug = Event.objects.get(slug=slug)
            event_by_slug.delete()
            return JsonResponse("Event deleted successfully", safe=False)
        except:
            return JsonResponse("Failed to delete event", safe=False)


# Uploading completion templates
class UploadCompletionTemplateView(APIView):
    def get(self, request):
        image_file = CompletionCertificateTemplate.objects.filter(
            user=request.user)

        if image_file:
            image_serializer = CompletionCertificateSerializer(
                image_file, many=True)
            return JsonResponse(image_serializer.data, safe=False)
        return JsonResponse("Failed to get images", safe=False)

    def post(self, request):
        try:
            file = request.FILES['pptx_file']
            contribute = request.data['contribute']

            if contribute == "true":
                ContributedCompletionCertificates.objects.create(
                    template=file).save()
            else:
                user = request.user.id
                user_id = User.objects.get(id=user)
                CompletionCertificateTemplate.objects.create(
                    user=user_id, template=file).save()

            return JsonResponse("Completion template uploaded successfully", safe=False)
        except:
            return JsonResponse("Failed to uploaded completion template", safe=False)


# Uploading merit templates
class UploadMeritTemplateView(APIView):
    def get(self, request):
        image_file = MeritCertificateTemplate.objects.filter(
            user=request.user)

        if image_file:
            image_serializer = MeritCertificateSerializer(
                image_file, many=True)
            return JsonResponse(image_serializer.data, safe=False)
        return JsonResponse("Failed to get images", safe=False)

    def post(self, request):
        try:
            file = request.FILES['pptx_file']
            contribute = request.data['contribute']

            if contribute == "true":
                ContributedMeritCertificates.objects.create(
                    template=file).save()
            else:
                user = request.user.id
                user_id = User.objects.get(id=user)
                MeritCertificateTemplate.objects.create(
                    user=user_id, template=file).save()

            return JsonResponse("Merit template uploaded successfully", safe=False)
        except:
            return JsonResponse("Failed to uploaded completion template", safe=False)


# Upload contribute completion templates
class ContributeCompletionView(APIView):
    def get(self, request):
        contribute_img = ContributedCompletionCertificates.objects.all()

        if contribute_img:
            contribute_img_serializers = ContributeCompletionCertificateSerializer(
                contribute_img, many=True)
            return JsonResponse(contribute_img_serializers.data, safe=False)
        return JsonResponse("Failed to get images", safe=False)


# Upload contribute merit certificate
class ContributeMeritView(APIView):
    def get(self, request):
        contribute_img = ContributedMeritCertificates.objects.all()

        if contribute_img:
            contribute_img_serializers = ContributeMeritCertificateSerializer(
                contribute_img, many=True)
            return JsonResponse(contribute_img_serializers.data, safe=False)
        return JsonResponse("Failed to get images", safe=False)


# Upload and get participant image album
class ParticipantImageAlbumView(APIView):
    def get(self, request, slug):
        image_album_slug = Event.objects.get(slug=slug)
        album_images = ParticipantAlbum.objects.filter(event=image_album_slug)

        if album_images:
            album_image_serializer = ImageAlbumSerializer(
                album_images, many=True)
            return JsonResponse(album_image_serializer.data, safe=False)
        return JsonResponse("Failed to get images", safe=False)

    def post(self, request, slug):
        try:
            album_images = request.FILES.getlist('album_images')
            event = Event.objects.get(slug=slug)

            for img in album_images:
                ParticipantAlbum.objects.create(
                    event=event, image_album=img)

            return JsonResponse("Image uploaded successfully", safe=False)
        except:
            return JsonResponse("Failed to upload image", safe=False)
