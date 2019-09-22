import graphene

from app import graph
from moc.graph.schema import Query as MocQuery

class Query(graph.Query, MocQuery,  graphene.ObjectType):
	pass


schema = graphene.Schema(query=Query)