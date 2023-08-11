from django.shortcuts import render, redirect
from .models import Course, Subscription, Payment
from .forms import SubscriptionForm, PaymentForm


# Create your views here.
def index(request):
    return render(request,'base.html')
def course_list(request):
    # user = request.user
    # Assuming you have a custom user profile model with the subscription information
    subscription_type = Subscription.subscription_type

    if subscription_type == 'Basic':
        courses = Course.objects.filter(level='Basic')
    elif subscription_type == 'Advanced':
        courses = Course.objects.filter(level='Advanced')
    else:  # 'Hybrid'
        courses = Course.objects.all()

    context = {'courses': courses}
    return render(request, 'course_list.html', context)

def subscription(request):
    user = request.user
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription_type = form.cleaned_data['subscription_type']
            subscription = Subscription.objects.create(subscription_type=subscription_type)
            return redirect('payment', subscription_id=subscription.id)
    else:
        form = SubscriptionForm()

    return render(request, 'subscription.html', {'form': form})

def payment(request, subscription_id):
    subscription = Subscription.objects.get(id=subscription_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment_method = form.cleaned_data['payment_method']
            Payment.objects.create(subscription_type=subscription.subscription_type, payment_method=payment_method)
            # Add logic here to grant access to courses based on the subscription
            return redirect('course_list')
    else:
        form = PaymentForm()

    return render(request, 'payment.html', {'form': form})




