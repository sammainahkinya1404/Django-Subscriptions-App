from django.urls import path
from . import views


urlpatterns = [
 path('initiate_payment/', views.initiate_payment, name='initiate_payment'),

 ]
 