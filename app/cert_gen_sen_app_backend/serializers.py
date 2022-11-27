from .models import *
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def create(self,validated_data):
        event = Event.objects.create(event_name=validated_data['event_name'],subject=validated_data['subject'],from_date=validated_data['from_date'],to_date=validated_data['to_date'],xlsx_file=validated_data['xlsx_file'])
        event.save()
        return event

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        models = Participant
        fields = '__all__'