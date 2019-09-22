from graphene_django.filter import DjangoFilterConnectionField
import graphene

from moc.graph.types import *


class Query(object):
	post = graphene.relay.Node.Field(PostType)
	all_posts = DjangoFilterConnectionField(PostType)

	blog = graphene.relay.Node.Field(BlogType)
	all_blogs = DjangoFilterConnectionField(BlogType)