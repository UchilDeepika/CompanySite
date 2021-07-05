from django.conf.urls import include
from django.urls.conf import path
from .import views

urlpatterns = [
  path('home',views.home,name='home'),
  path('aboutus',views.aboutus,name='aboutus'),
  path('contactus',views.contactus,name='contactus'),
  path('',views.home,name='home'),
]