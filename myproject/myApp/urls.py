from django.contrib import path
from django.conf import settings
from .import views

urlpatterns = [
     path('',views.index,name='index'),
 ]
 