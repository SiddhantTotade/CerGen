from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
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
# from .serializers import UserSerializer, RegisterSerializer
from .helpers import *
from itertools import islice
from collections import OrderedDict
import openpyxl


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
        return Response({'msg': 'Password changed successfully'}, status=status.HTTP_200_OK)


# User send password-reset link view
class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, reuqest, format=None):
        serializer = UserSendPasswordResetEmailSerializer(data=reuqest.data)

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
# def generate_uid(stu_id, eve_name, eve_dept, eve_date):
#     random_num = random.randint(1000, 9999)
#     certificate_id = str(stu_id)+str(eve_name)+str(eve_dept) + \
#         str(eve_date).replace("-", "")+str(random_num)
#     return certificate_id


# ManageUser API
# class ManageUserAPI(generics.RetrieveUpdateAPIView):
#     serializer_class = UserSerializer
#     permission_classes = (permissions.IsAuthenticated,)

#     def get_object(self):
#         return self.request.user


# Login API
# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)


# Register API
# class RegisterAPI(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#             "user": UserSerializer(user, context=self.get_serializer_context()).data,
#             "token": AuthToken.objects.create(user)[1]
#         })


# Getting all events view
class EventsOperations(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_events = reversed(Event.objects.filter(user=request.user))

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


# Upload participant image
class UploadParticipantImage(APIView):
    def patch(self, request, pk):
        participant_img = request.data['participant_image']
        Participant.objects.filter(id=pk).update(student_image=participant_img)

        return JsonResponse("Image uploaded successfully", safe=False)


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


# Uploading completion templates
class UploadCompletionTemplate(APIView):
    def get(self, request):
        image_file = CompletionCertificateTemplate.objects.filter(
            user=request.user.id)

        if image_file:
            image_serializer = CompletionCertificateSerializer(
                image_file, many=True)
            return JsonResponse(image_serializer.data, safe=False)
        return JsonResponse("Failed to get images", safe=False)

    def post(self, request):
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


# Uploading merit templates
class UploadMeritTemplate(APIView):
    def get(self, request):
        image_file = MeritCertificateTemplate.objects.filter(
            user=request.user.id)

        if image_file:
            image_serializer = MeritCertificateSerializer(
                image_file, many=True)
            return JsonResponse(image_serializer.data, safe=False)
        return JsonResponse("Failed to get images", safe=False)

    def post(self, request):
        file = request.FILES['pptx_file']
        contribute = request.data['contribute']

        if contribute == "true":
            ContributedMeritCertificates.objects.create(template=file).save()
        else:
            user = request.user.id
            user_id = User.objects.get(id=user)
            MeritCertificateTemplate.objects.create(
                user=user_id, template=file).save()

        return JsonResponse("Merit template uploaded successfully", safe=False)


# Upload contribute completion templates
class ContributeCompletion(APIView):
    def get(self, request):
        contribute_img = ContributedCompletionCertificates.objects.all()

        if contribute_img:
            contribute_img_serializers = ContributeCompletionCertificateSerializer(
                contribute_img, many=True)
            return JsonResponse(contribute_img_serializers.data, safe=False)
        return JsonResponse("Failed to get images", safe=False)


# Upload contribute merit certificate
class ContributeMerit(APIView):
    def get(self, request):
        contribute_img = ContributedMeritCertificates.objects.all()

        if contribute_img:
            contribute_img_serializers = ContributeMeritCertificateSerializer(
                contribute_img, many=True)
            return JsonResponse(contribute_img_serializers.data, safe=False)
        return JsonResponse("Failed to get images", safe=False)


# Upload and get participant image album
class ParticipantImageAlbum(APIView):
    def get(self, request, slug):
        image_album_slug = Event.objects.get(slug=slug)
        album_images = ParticipantAlbum.objects.filter(event=image_album_slug)

        if album_images:
            album_image_serializer = ImageAlbumSerializer(
                album_images, many=True)
            return JsonResponse(album_image_serializer.data, safe=False)
        return JsonResponse("Failed to get images", safe=False)

    def post(self, request, slug):
        album_images = request.FILES.getlist('album_images')
        event = Event.objects.get(slug=slug)

        for img in album_images:
            ParticipantAlbum.objects.create(
                event=event, image_album=img)

            return JsonResponse("Image uploaded successfully", safe=False)
        return JsonResponse("Failed to upload image", safe=False)
