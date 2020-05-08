from django.urls import path
from myapp2 import views
urlpatterns=[
	path('',views.hello,name='hello'),
	path('register/',views.register,name='register'),
	path('details/',views.details,name='details'),
	path('edit/<int:id>',views.edit,name='edit'),
	path('account',views.account,name='account'),
]