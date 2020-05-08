from django.contrib import admin
from myapps.models import User
# Register your models here.
class Ad(admin.ModelAdmin):
	list_display = ['firstName','lastName','userName','mailId','phoneNumber','age']
admin.site.register(User,Ad)
