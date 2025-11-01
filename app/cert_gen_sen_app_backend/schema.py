import graphene
from graphene_django import DjangoObjectType
from .models import Participant, Event


class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = ("id", "user", "event", "details")


class EventQuery(graphene.ObjectType):
    events = graphene.List(EventType)

    def resolve_events(self, info):
        user = info.context.user

        if user.is_authenticated():
            return Event.objects.filter(user_id=user)

        return Event.objects.none()


# class ParticipantType(DjangoObjectType):
#     class Meta:
#         fields = ("id", "participants_details", "event")


# class Query(graphene.ObjectType):
#     participants = graphene.List(ParticipantType, event_id=graphene.Int(required=False))

#     def resolve_participants(self, info, event_id=None):
#         qs = Participant.objects.filter(event_id=event_id)

#         return qs


# schema = graphene.Schema(query=Query)
