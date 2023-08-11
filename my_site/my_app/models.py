from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Payment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    method = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100)
    # Add other necessary fields for tracking payment details