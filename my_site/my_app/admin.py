from django.contrib import admin
from .models import Course, Payment

class CourseAdmin(admin.ModelAdmin):
    list_display =('name','price')
admin.site.register(Course,CourseAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display =('course','method','transaction_id')
# Register your models here.
admin.site.register(Payment,PaymentAdmin)
