from django.contrib import admin
from .models import Course, Subscription, Payment

admin.site.register(Course)
admin.site.register(Subscription)
admin.site.register(Payment)
