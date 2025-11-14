from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.template import Template as DjangoTemplate, Context
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import *
from .models import *
from .serializers import *
from .resources import *
from .helpers import *
from itertools import islice
from collections import OrderedDict
from .services.grpc_client import generate_pdf_via_grpc
from cergen_auth.authentication import CustomJWTAuthentication
from graphene_django.views import GraphQLView
import openpyxl
import base64


class AuthenticatedGraphQlView(GraphQLView):
    def dispatch(self, request, *args, **kwargs):
        user = None
        auth_classes = [CustomJWTAuthentication]

        for auth_class in auth_classes:
            auth = auth_class()
            try:
                user_auth_tuple = auth.authenticate(request)
                if user_auth_tuple:
                    user, _ = user_auth_tuple
                    break
            except Exception as e:
                print("Auth error:", e)
        request.user = user or request.user
        return super().dispatch(request, *args, **kwargs)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import base64

from .models import Event, Template
from .helpers import TemplateRenderHelper
from types import SimpleNamespace


def dict_to_namespace(data):
    if isinstance(data, dict):
        return SimpleNamespace(**{k: dict_to_namespace(v) for k, v in data.items()})
    elif isinstance(data, list):
        return [dict_to_namespace(v) for v in data]
    else:
        return data


class GenerateEventTemplateAPIView(APIView):
    def post(self, request):
        try:
            event_id = request.data.get("event_id")
            template_id = request.data.get("template_id")
            orientation = request.data.get("orientation", "portrait")

            if not event_id or not template_id:
                return Response(
                    {
                        "success": False,
                        "message": "event_id and template_id are required.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            event = Event.objects.get(id=event_id)
            template_obj = Template.objects.get(id=template_id, user=event.user)

            event_details = {}
            if hasattr(event, "details") and event.details:
                try:
                    if isinstance(event.details, str):
                        event_details = json.loads(event.details)
                    elif isinstance(event.details, dict):
                        event_details = event.details
                except Exception as e:
                    print("Invalid JSON in event.details:", e)

            event_obj = dict_to_namespace(event_details)

            html_template = DjangoTemplate(template_obj.html_content or "")
            context = Context({"e": event_obj})
            rendered_html = html_template.render(context)

            html_clean = rendered_html.replace("\r", "").replace("\n", "")
            pdf_bytes = generate_pdf_via_grpc(template_id, html_clean, orientation)
            encoded_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

            return Response(
                {
                    "success": True,
                    "message": "Event template generated successfully.",
                    "data": {
                        "html": rendered_html,
                        "pdf_data": encoded_pdf,
                    },
                },
                status=status.HTTP_200_OK,
            )

        except Event.DoesNotExist:
            return Response(
                {"success": False, "message": "Event not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Template.DoesNotExist:
            return Response(
                {"success": False, "message": "Template not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


import json
import base64
from django.template import Template as DjangoTemplate, Context
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event, Template, Participant


class GenerateEventTemplatesAPIView(APIView):
    def post(self, request):
        try:
            event_id = request.data.get("event_id")
            template_id = request.data.get("template_id")
            orientation = request.data.get("orientation", "portrait")

            if not event_id or not template_id:
                return Response(
                    {
                        "success": False,
                        "message": "event_id and template_id are required.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            event = Event.objects.get(id=event_id)
            template_obj = Template.objects.get(id=template_id, user=event.user)

            event_details = {}
            if event.details:
                try:
                    if isinstance(event.details, str):
                        event_details = json.loads(event.details)
                    elif isinstance(event.details, dict):
                        event_details = event.details
                except Exception as e:
                    print("Invalid JSON in event.details:", e)

            event_obj = dict_to_namespace(event_details)

            participants = Participant.objects.filter(event=event)
            if not participants.exists():
                return Response(
                    {
                        "success": False,
                        "message": "No participants found for this event.",
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

            rendered_outputs = []

            for participant in participants:
                participant_details = {}
                if participant.participant_details:
                    try:
                        if isinstance(participant.participant_details, str):
                            participant_details = json.loads(
                                participant.participant_details
                            )
                        elif isinstance(participant.participant_details, dict):
                            participant_details = participant.participant_details
                    except Exception as e:
                        print("Invalid JSON in participant_details:", e)

                participant_obj = dict_to_namespace(participant_details)

                html_template = DjangoTemplate(template_obj.html_content or "")
                context = Context({"e": event_obj, "p": participant_obj})
                rendered_html = html_template.render(context)
                html_clean = rendered_html.replace("\r", "").replace("\n", "")

                pdf_bytes = generate_pdf_via_grpc(template_id, html_clean, orientation)
                encoded_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

                rendered_outputs.append(
                    {
                        "participant_id": participant.id,
                        "html": rendered_html,
                        "pdf_data": encoded_pdf,
                    }
                )

            return Response(
                {
                    "success": True,
                    "message": "Templates generated for all participants.",
                    "data": rendered_outputs,
                },
                status=status.HTTP_200_OK,
            )

        except Event.DoesNotExist:
            return Response(
                {"success": False, "message": "Event not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        except Template.DoesNotExist:
            return Response(
                {"success": False, "message": "Template not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            print("Unexpected error:", e)
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class GenerateParticipantTemplateAPIView(APIView):

    def post(self, request):
        try:
            event_id = request.data.get("event_id")
            template_id = request.data.get("template_id")
            participant_id = request.data.get("participant_id")

            if not event_id or not template_id or not participant_id:
                return Response(
                    {
                        "success": False,
                        "message": "event_id, template_id, and participant_id are required.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            event = Event.objects.get(id=event_id)
            template_obj = Template.objects.get(id=template_id, user=event.user)
            participant = Participant.objects.get(id=participant_id, event=event)

            html = TemplateRenderHelper.render_html(
                template_obj.html_content, event, participant
            )

            return HttpResponse(html)

        except (
            Event.DoesNotExist,
            Participant.DoesNotExist,
            Template.DoesNotExist,
        ):
            return Response(
                {
                    "success": False,
                    "message": "Invalid event, participant, or template.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class EventView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        events = Event.objects.filter(user=request.user).order_by("-id")

        if events:
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Events not found", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = EventSerializer(data=request.data, context={"request": request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        event_id = request.data.get("id")

        if not event_id:
            return Response(
                {"error": "Event ID is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        event = get_object_or_404(Event, id=event_id, user=request.user)
        serializer = EventSerializer(
            event, data=request.data, partial=True, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        event_id = request.data.get("id")

        if not event_id:
            return Response(
                {"error": "Event ID is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        event = get_object_or_404(Event, id=event_id, user=request.user)
        event.delete()

        return Response("Event deleted", status=status.HTTP_204_NO_CONTENT)


class ParticipantsView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        event_id = request.query_params.get("event")

        if not event_id:
            return Response(
                {"error": "Event ID is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        event = get_object_or_404(Event, id=event_id, user=request.user)

        participants = Participant.objects.filter(event=event)

        serializer = ParticipantSerializer(participants, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        event_id = request.query_params.get("event")

        if not event_id:
            return Response({"error": "Event ID is required"}, status=400)

        data = request.data.copy()
        data["event"] = event_id

        serializer = ParticipantSerializer(data=data, context={"request": request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        participant_id = request.query_params.get("participant")

        if not participant_id:
            return Response(
                {"error": "Participant ID is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        participant = get_object_or_404(
            Participant, id=participant_id, event__user=request.user
        )

        participant_details = request.data.get("participant_details")

        if participant_details is None:
            return Response(
                {"error": "Participant details is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        participant.participant_details = participant_details
        participant.save(update_fields=["participant_details"])

        serializer = ParticipantSerializer(participant)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        participant_id = request.data.get("id")

        if not participant_id:
            return Response(
                {"error": "Participant ID is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        participant = get_object_or_404(
            Participant, id=participant_id, event__user=request.user
        )

        participant.delete()

        return Response(
            {"message": "Participant deleted successfully"}, status=status.HTTP_200_OK
        )


class TemplateView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        templates = Template.objects.filter(user=request.user).order_by("-id")

        if templates:
            serializer = TemplateSerializer(templates, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Templates not found", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = TemplateSerializer(data=request.data, context={"request": request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        template_id = request.data.get("id")

        if not template_id:
            return Response(
                {"error": "Template ID is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        template = get_object_or_404(Template, id=template_id, user=request.user)
        serializer = TemplateSerializer(
            template, data=request.data, partial=True, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pass


class TemplateDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, template_id):
        template = get_object_or_404(Template, id=template_id, user=request.user)
        serializer = TemplateSerializer(template)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SenderCredentialView(APIView):
    def get(self, request):
        try:
            user_id = request.user.id

            if SendersCredentials.objects.filter(user=user_id).exists():
                return JsonResponse(1, safe=False)
            return JsonResponse(0, safe=False)
        except:
            return JsonResponse("Something went wrong", safe=False)

    def post(self, request):
        try:
            user_id = request.user.id
            user = User.objects.get(id=user_id)

            if SendersCredentials.objects.filter(user=user_id).exists():
                SendersCredentials.objects.update(
                    user=user,
                    senders_email=request.data["email"],
                    senders_password=request.data["password"],
                    senders_phone=request.data["phone"],
                )
            else:
                SendersCredentials.objects.create(
                    user=user,
                    senders_email=request.data["email"],
                    senders_password=request.data["password"],
                    senders_phone=request.data["phone"],
                )

            return JsonResponse("Sender credentials saved successfully", safe=False)
        except:
            return JsonResponse("Failed to save credentials", safe=False)


# Getting all events view
class EventsView(APIView):
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

    def put(self, request, pk):
        event_id = Event.objects.get(id=pk)
        event_serialized_data = EventSerializer(
            instance=event_id, data=request.data, partial=True
        )

        if event_serialized_data.is_valid():
            event_serialized_data.save()
            return JsonResponse("Event updated successfully", safe=False)
        return JsonResponse("Failed to update event", safe=False)


# Getting data from xlsx and uploading to database
class UploadParticipantView(APIView):
    def get(self, request):
        all_participants = Participant.objects.all()

        if all_participants:
            participant_serializer = ParticipantSerializer(all_participants, many=True)
            return JsonResponse(participant_serializer.data, safe=False)
        return JsonResponse("No participant data", safe=False)

    def post(self, request):
        try:
            event_id = request.data["event_id"]
            participant_file = request.data["participants_file"]

            wb = openpyxl.load_workbook(participant_file)
            work_sheet = wb["Form Responses 1"]

            excel_data = list()
            for row in islice(work_sheet.values, 1, work_sheet.max_row):
                data = OrderedDict()
                data["id"] = row[0]
                data["Full_Name"] = row[1]
                data["Participant_Id"] = row[2]
                data["Email"] = row[3]
                data["Phone"] = row[4]
                data["Certificate_Status"] = row[5]
                excel_data.append(data)

            eve_id = Event.objects.filter(id=event_id)
            event_new_id = Event.objects.get(id=event_id)

            event_name = ""
            event_dept = ""
            event_date = ""

            for eve in eve_id:
                event_name = eve.event_name
                event_dept = eve.event_department
                event_date = eve.from_date

            event_name_words = event_name.split()
            event_name_chars_list = [word[0] for word in event_name_words]
            event_name_chars_string = "".join(event_name_chars_list)

            participants_list = []

            for data in excel_data:
                participant_name = data["Full_Name"]
                participant_id = data["Participant_Id"]
                email = data["Email"]
                phone = data["Phone"]
                if "+91" in str(phone):
                    phone = data["Phone"]
                else:
                    phone = "+91" + str(data["Phone"])
                certificate_status = data["Certificate_Status"]
                certificate_id = generate_uid(
                    data["Participant_Id"],
                    event_name_chars_string,
                    event_dept,
                    event_date,
                )
                participants_list.append(
                    Participant(
                        event=event_new_id,
                        participant_name=participant_name,
                        participant_id=participant_id,
                        email=email,
                        phone=phone,
                        certificate_status=certificate_status,
                        certificate_id=certificate_id,
                    )
                )

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
            instance=participant_by_id, data=request.data, partial=True
        )

        if participant_serialized_data.is_valid():
            participant_serialized_data.save()
            return JsonResponse("Participant updated successfully", safe=False)
        return JsonResponse("Failed to update participant", safe=False)


# Upload participant image
class UploadParticipantImageView(APIView):
    def patch(self, request, pk):
        try:
            participant_img = request.FILES["participant_image"]
            image = Participant.objects.get(id=pk)
            image.participant_image = participant_img
            image.save()

            return JsonResponse("Image uploaded successfully", safe=False)
        except:
            return JsonResponse("Failed to uploaded image", safe=False)


# Filtering events by slug
@permission_classes((IsAuthenticated,))
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
        image_file = CompletionCertificateTemplate.objects.filter(user=request.user)

        if image_file:
            image_serializer = CompletionCertificateSerializer(image_file, many=True)
            return JsonResponse(image_serializer.data, safe=False)
        return JsonResponse("Failed to get images", safe=False)

    def post(self, request):
        try:
            file = request.FILES["pptx_file"]
            contribute = request.data["contribute"]

            if contribute == "true":
                ContributedCompletionCertificates.objects.create(template=file).save()
            else:
                user = request.user.id
                user_id = User.objects.get(id=user)
                CompletionCertificateTemplate.objects.create(
                    user=user_id, template=file
                ).save()

            return JsonResponse("Completion template uploaded successfully", safe=False)
        except:
            return JsonResponse("Failed to uploaded completion template", safe=False)


# Uploading merit templates
class UploadMeritTemplateView(APIView):
    def get(self, request):
        image_file = MeritCertificateTemplate.objects.filter(user=request.user)

        if image_file:
            image_serializer = MeritCertificateSerializer(image_file, many=True)
            return JsonResponse(image_serializer.data, safe=False)
        return JsonResponse("Failed to get images", safe=False)

    def post(self, request):
        try:
            file = request.FILES["pptx_file"]
            contribute = request.data["contribute"]

            if contribute == "true":
                ContributedMeritCertificates.objects.create(template=file).save()
            else:
                user = request.user.id
                user_id = User.objects.get(id=user)
                MeritCertificateTemplate.objects.create(
                    user=user_id, template=file
                ).save()

            return JsonResponse("Merit template uploaded successfully", safe=False)
        except:
            return JsonResponse("Failed to uploaded completion template", safe=False)


# Upload contribute completion templates
class ContributeCompletionView(APIView):
    def get(self, request):
        contribute_img = ContributedCompletionCertificates.objects.all()

        if contribute_img:
            contribute_img_serializers = ContributeCompletionCertificateSerializer(
                contribute_img, many=True
            )
            return JsonResponse(contribute_img_serializers.data, safe=False)
        return JsonResponse("Failed to get images", safe=False)


# Upload contribute merit certificate
class ContributeMeritView(APIView):
    def get(self, request):
        contribute_img = ContributedMeritCertificates.objects.all()

        if contribute_img:
            contribute_img_serializers = ContributeMeritCertificateSerializer(
                contribute_img, many=True
            )
            return JsonResponse(contribute_img_serializers.data, safe=False)
        return JsonResponse("Failed to get images", safe=False)


# Upload and get participant image album
class ParticipantImageAlbumView(APIView):
    def get(self, request, slug):
        image_album_slug = Event.objects.get(slug=slug)
        album_images = ParticipantAlbum.objects.filter(event=image_album_slug)

        if album_images:
            album_image_serializer = ImageAlbumSerializer(album_images, many=True)
            return JsonResponse(album_image_serializer.data, safe=False)
        return JsonResponse("Failed to get images", safe=False)

    def post(self, request, slug):
        try:
            album_images = request.FILES.getlist("album_images")
            event = Event.objects.get(slug=slug)

            for img in album_images:
                ParticipantAlbum.objects.create(event=event, image_album=img)

            return JsonResponse("Image uploaded successfully", safe=False)
        except:
            return JsonResponse("Failed to upload image", safe=False)
