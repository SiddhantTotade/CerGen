from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from rest_framework import serializers
from rest_framework import serializers
from xml.dom import ValidationErr
from .models import *
from .renderers import *
from .utils import *


class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "event", "details"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


# Sender credential serializer
class SenderCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendersCredentials
        fields = "__all__"


# Event serializer
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    def create(self, validated_data):
        event = Event.objects.create(
            user=validated_data["user"],
            event_name=validated_data["event_name"],
            subject=validated_data["subject"],
            event_department=validated_data["event_department"],
            from_date=validated_data["from_date"],
            to_date=validated_data["to_date"],
            event_year=validated_data["event_year"],
        )
        event.save()
        return event


# Participant serializer
class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = "__all__"


# Participant image serializer
class ParticipantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ["participant_image"]

    def update(self, validated_data):
        participant_img = Participant.objects.update(
            student_image=validated_data["participant_image"]
        )
        participant_img.save()
        return participant_img


# Completion certificate serializer
class CompletionCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletionCertificateTemplate
        fields = ["template_img"]


# Merit Certificate serializer
class MeritCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeritCertificateTemplate
        fields = ["template_img"]


#  Contribution completion certificate serializer
class ContributeCompletionCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributedCompletionCertificates
        fields = ["template_img"]


#  Contribution merit certificate serializer
class ContributeMeritCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributedMeritCertificates
        fields = ["template_img"]


#  Image album serializer
class ImageAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantAlbum
        fields = "__all__"

    def create(self, validated_data):
        album_image = ParticipantAlbum.objects.create(
            event=validated_data["event"], image_album=validated_data["album_images"]
        )
        album_image.save()
        return album_image
