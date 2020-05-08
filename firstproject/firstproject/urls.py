"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from myapp import views as v2
from firstapp import views    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/',views.hi,name='hi',),
    path('hello/<str:name>',views.hello,name ='hello'),
    path('rollno/<int:id>',views.rollno,name='rollno'),
    path('mesage/',views.message,name = 'message'),
    path('register/',views.register,name ='register'),
    path('details/',views.details,name = 'userDetails'),
    path('registrationForm',views.registrationForm,name = 'registrationForm'),
    path('restaurantapp',views.restaurantapp,name = 'restaurantapp'),
    path('signup',views.signup,name='signup'),
    path('showAll/',views.showAll,name='showAll'),
    path('myapp/',include('myapp.urls')),
    

]
