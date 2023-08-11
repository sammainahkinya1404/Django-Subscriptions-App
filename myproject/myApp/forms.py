# courses/forms.py
from django import forms

class SubscriptionForm(forms.Form):
    SUBSCRIPTION_CHOICES = (
        ('Basic', 'Basic'),
        ('Advanced', 'Advanced'),
        ('Hybrid', 'Hybrid'),
    )
    subscription_type = forms.ChoiceField(choices=SUBSCRIPTION_CHOICES, widget=forms.RadioSelect)

class PaymentForm(forms.Form):
    PAYMENT_CHOICES = (
        ('MPesa', 'MPesa'),
        ('Paypal', 'Paypal'),
    )
    payment_method = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.RadioSelect)
