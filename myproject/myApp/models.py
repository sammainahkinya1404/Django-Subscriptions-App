from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    LEVEL_CHOICES = (
        ('Basic', 'Basic'),
        ('Advanced', 'Advanced'),
    )

    title = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    description = models.TextField()
    video_url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class Subscription(models.Model):
    SUBSCRIPTION_CHOICES = (
        ('Basic', 'Basic'),
        ('Advanced', 'Advanced'),
        ('Hybrid', 'Hybrid'),
    )

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=20, choices=SUBSCRIPTION_CHOICES)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.user.username} - {self.subscription_type}"

class Payment(models.Model):
    PAYMENT_CHOICES = (
        ('MPesa', 'MPesa'),
        ('Paypal', 'Paypal'),
    )
    SUBSCRIPTION_CHOICES = (
        ('Basic', 'Basic'),
        ('Advanced', 'Advanced'),
        ('Hybrid','Hybrid')
    )

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=20, choices=SUBSCRIPTION_CHOICES)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.subscription_type} - {self.payment_method}"
