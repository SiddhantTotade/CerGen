from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
# User Serializer
# class UserRegistrationSerializer(serializers.ModelSerializer):
#     passowrd2 = serializers.CharField(
#         style={'input_type': 'password'}, write_only=True
#     )

#     class Meta:
#         model = User
#         fields = ('email', 'name', 'password', 'password2', 'tc')
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

#     def validate(self, attrs):
#         password = attrs.get('password')
#         password2 = attrs.get('password2')
#         return super().validate(attrs)

# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        event = Event.objects.create(user=validated_data['user'], event_name=validated_data['event_name'], subject=validated_data['subject'],
                                     event_department=validated_data['event_department'], from_date=validated_data['from_date'], to_date=validated_data['to_date'], event_year=validated_data['event_year'])
        event.save()
        return event


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

    def create(self, validated_data):
        event = Participant.objects.create(event=validated_data['event'], student_name=validated_data['student_name'],
                                           student_id=validated_data['student_id'], email=validated_data['email'], certificate_status=validated_data['certificate_status'])
        event.save()
        return event
