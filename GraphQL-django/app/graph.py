from app.models import Customer, Product, Order

from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import graphene

class CustomerType(DjangoObjectType):
	class Meta:
		model = Customer
		filter_fields = {
			'id':['exact'],
			'name': ['exact', 'icontains', 'istartswith'],
			'phone':['exact',], 
			'email':['exact']
		}
		interfaces = (graphene.relay.Node, )


class ProductType(DjangoObjectType):
	class Meta:
		model = Product



class OrderType(DjangoObjectType):
	class Meta:
		model = Order


class Query(object):
	customer = graphene.relay.Node.Field(CustomerType)
	all_customers = DjangoFilterConnectionField(CustomerType)
	
	all_products = graphene.List(ProductType)
	all_orders = graphene.List(OrderType)

	def resolve_all_customers(self, info, **kwargs):
		return Customer.objects.all()

	def resolve_all_products(self, info, **kwargs):
		return Product.objects.all()


	def resolve_all_orders(self, info, **kwargs):
		return Order.objects.all()
