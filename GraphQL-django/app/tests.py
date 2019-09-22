from django.test import TestCase

# Create your tests here.
import json
from graphene_django.utils.testing import GraphQLTestCase
from app.schema import schema

class Hello(GraphQLTestCase):
	GRAPHQL_SCHEMA = schema
	print(schema)
	def test_some_query(self):
		response = self.query(
			'''
			query{
			  allProducts{
			    name
			    price
			    id
			  }
			}
						
			''',
			op_name = 'product'
		)
		print(response.content)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)