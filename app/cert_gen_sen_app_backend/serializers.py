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

# User registration serializer


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'tc']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password is not matching")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


# User login serializer
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']


# User profile serializer
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name']


# User change password
class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        max_length=255, style={'input_type': 'password2'}, write_only=True)

    class Meta:
        model = User
        fields = ['password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')

        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password is not matching")

        user.set_password(password)
        user.save()
        return attrs


# User reset password email
class UserSendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            link = f'http://localhost:3000/api/user/reset-password/{uid}/{token}'
            body = f'Click on the link to reset password - {link}'
            data = {
                'email_subject': 'Reset your password',
                'email_body': body,
                'to_email': user.email
            }
            Util.send_email(data)
            return attrs
        else:
            raise serializers.ValidationError("You are not a registered admin")


# User reset password
class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        max_length=255, style={'input_type': 'password2'}, write_only=True)

    class Meta:
        model = User
        fields = ['password', 'password2']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')

            if password != password2:
                raise serializers.ValidationError("Password does not matching")

            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise ValidationErr("Token is not valid")

            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise ValidationErr("Token is not valid")


# Sender credential serializer
class SenderCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendersCredentials
        fields = '__all__'


# Event serializer
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        event = Event.objects.create(user=validated_data['user'], event_name=validated_data['event_name'], subject=validated_data['subject'],
                                     event_department=validated_data['event_department'], from_date=validated_data['from_date'], to_date=validated_data['to_date'], event_year=validated_data['event_year'])
        event.save()
        return event


# Participant serializer
class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'


# Participant image serializer
class ParticipantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['participant_image']

    def update(self, validated_data):
        participant_img = Participant.objects.update(
            student_image=validated_data['participant_image'])
        participant_img.save()
        return participant_img


# Completion certificate serializer
class CompletionCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletionCertificateTemplate
        fields = ['template_img']


# Merit Certificate serializer
class MeritCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeritCertificateTemplate
        fields = ['template_img']


#  Contribution completion certificate serializer
class ContributeCompletionCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributedCompletionCertificates
        fields = ['template_img']


#  Contribution merit certificate serializer
class ContributeMeritCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributedMeritCertificates
        fields = ['template_img']


#  Image album serializer
class ImageAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantAlbum
        fields = '__all__'

    def create(self, validated_data):
        album_image = ParticipantAlbum.objects.create(
            event=validated_data['event'], image_album=validated_data['album_images'])
        album_image.save()
        return album_image
