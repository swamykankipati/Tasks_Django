from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=33)
    lastName = models.CharField(max_length=33)
    userName = models.CharField(max_length=23)
    password = models.CharField(max_length=50)
    mailId = models.CharField(max_length=53)
    phoneNumber = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return str(self.id)+' '+self.lastName
    # def __str__(self):
    #     return self.empid+' '+self.empName
