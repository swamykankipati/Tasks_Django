from django.db import models


class Emp(models.Model):
	first_name = models.CharField(max_length = 30,null=True)
	last_name = models.CharField(max_length = 50)
	age = models.IntegerField(null=True)

	def __str__(self):

		return self.last_name+' '+self.first_name+' '+str(self.age)

class employee(models.Model):
	empid = models.IntegerField(max_length = 10)
	empName = models.CharField(max_length = 50)
	empDesign = models.CharField(max_length = 50)
	salary = models.FloatField(null=True)

	def __str__(self):

		return self.empid+' '+self.empName