from django.db import models

class Customer(models.Model):
	name = models.CharField(max_length=40)
	phone = models.CharField(max_length=11, unique=True)
	email = models.EmailField(unique=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=6, unique=True)
	price = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.code

class Order(models.Model):
	customer = models.ForeignKey(Customer,related_name='customer', on_delete=models.CASCADE)
	product = models.ForeignKey(Product,related_name='product', on_delete=models.CASCADE)
	quantity = models.PositiveSmallIntegerField(default=1)
	ammount = models.PositiveIntegerField()