from .models import *
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def create(self,validated_data):
        event = Event.objects.create(user=validated_data['user'],event_name=validated_data['event_name'],subject=validated_data['subject'],from_date=validated_data['from_date'],to_date=validated_data['to_date'])
        event.save()
        return event

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'
    
    def create(self,validated_data):
        event = Participant.objects.create(event=validated_data['event'],student_name=validated_data['student_name'],email=validated_data['email'],certificate_status=validated_data['certificate_status'])
        event.save()
        return event