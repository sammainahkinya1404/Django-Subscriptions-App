from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('courses',views.course,name='course'),
    path('payment',views.payment,name='payment'),
    path('payment_status',views.payment_status,name='payment_status'),
    path('bundle',views.bundle,name='bundle'),
    path('',views.index,name='index'),
    path('daraja/stk-push', views.stk_push_callback, name='mpesa_stk_push_callback'),
    path('payment_callback', views.payment_callback, name='payment_callback'),
    
]
