from django.urls import path
from locate.views import *
from . import views

urlpatterns = [
  path('', views.home, name='home'),
]