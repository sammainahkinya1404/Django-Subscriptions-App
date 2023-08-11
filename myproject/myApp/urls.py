from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('course_list', views.course_list, name='course_list'),
    path('subscription', views.subscription, name='subscription'),
    path('payment', views.payment, name='payment'),
 ]
 