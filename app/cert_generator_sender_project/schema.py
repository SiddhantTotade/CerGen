import graphene
from cert_gen_sen_app_backend.schema import EventQuery


class Query(EventQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
