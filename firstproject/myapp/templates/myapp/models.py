from django.db import models

# Create your models here.
class student(models.Model):
	branches = [('CSE','cse'),
				('ECE','ece'),
				('IT','it'),
				('EEE','eee')]
	stdid = models.IntegerField(max_length = 10)
	stdName = models.CharField(max_length = 50)
	branch = models.CharField(max_length = 50,choices=branches)
	age = models.IntegerField(null=True)

	