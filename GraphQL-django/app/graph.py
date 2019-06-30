from app.models import Customer, Product, Order

from graphene_django.types import DjangoObjectType
import graphene

class CustomerType(DjangoObjectType):
	class Meta:
		model = Customer


class ProductType(DjangoObjectType):
	class Meta:
		model = Product



class OrderType(DjangoObjectType):
	class Meta:
		model = Order


class Query(object):
	all_customers = graphene.List(CustomerType)
	all_products = graphene.List(ProductType)
	all_orders = graphene.List(OrderType)

	def resolve_all_customers(self, info, **kwargs):
		return Customer.objects.all()

	def resolve_all_products(self, info, **kwargs):
		return Product.objects.all()


	def resolve_all_orders(self, info, **kwargs):
		return Order.objects.all()
