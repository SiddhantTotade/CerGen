import graphene
from graphene_django import DjangoObjectType
from .models import Participant, Event


class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = ("id", "title", "date")


class ParticipantType(DjangoObjectType):
    class Meta:
        fields = ("id", "participants_details", "event")


class Query(graphene.ObjectType):
    participants = graphene.List(ParticipantType, event_id=graphene.Int(required=False))

    def resolve_participants(self, info, event_id=None):
        qs = Participant.objects.filter(event_id=event_id)

        return qs


schema = graphene.Schema(query=Query)
