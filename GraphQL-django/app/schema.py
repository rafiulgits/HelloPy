import graphene

from app import graph

class Query(graph.Query,graphene.ObjectType):
	pass


schema = graphene.Schema(query=Query)