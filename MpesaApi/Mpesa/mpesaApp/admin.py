from django.contrib import admin
from .models import Transaction

# Register your models here.
# class TransAdmin(admin.ModelAdmin):
#     list_display = ('item','amount','phone_number','timestamp')
admin.site.register(Transaction)