from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField


class Post(models.Model):
	uid = models.AutoField(primary_key=True)
	tags = ArrayField(models.CharField(max_length=10))



class Blog(models.Model):
	uid = models.AutoField(primary_key=True)
	data = JSONField()




class Site(models.Model):
	uid = models.AutoField(primary_key=True)
	blogs = models.ManyToManyField(Blog)