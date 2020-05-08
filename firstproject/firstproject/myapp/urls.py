from django.urls import path
from myapp import views

urlpatterns = [
	path('',views.hello,name='hello'),
	path('register/',views.register,name='register'),
	path('details/',views.details,name='details'),
	# path('edit/',views.edit,name='edit'),
]