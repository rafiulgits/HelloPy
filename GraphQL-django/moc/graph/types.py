from moc.models import *
from graphene_django.types import DjangoObjectType
import graphene

class PostType(DjangoObjectType):
	class Meta:
		model = Post
		filter_fields = {
			'uid':['exact'],
		}
		interfaces = (graphene.relay.Node,)



class BlogType(DjangoObjectType):
	class Meta:
		model = Blog
		filter_fields = {
			'uid':['exact'],
		}
		interfaces = (graphene.relay.Node, )