from django.shortcuts import render,redirect

from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient

# Create your views here
def course(request):
     return render(request,'Courses.html')

def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0791848007'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push_callback(request):
        data = request.body
        
        return HttpResponse("STK Push in Django👋")

# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django_daraja.mpesa.core import MpesaClient
# from .models import Course

# def initiate_payment(request, course_id):
#     cl = MpesaClient()
#     course = Course.objects.get(id=course_id)
#     phone_number = '0791848007'  # Replace with the user's phone number
#     amount = course.price
#     account_reference = f'Payment for {course.name}'
#     transaction_desc = 'Description'
#     callback_url = 'https://your-domain.com/payment-callback'
#     response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
#     return HttpResponse(response)

# def payment_callback(request):
#     # Handle the response from Mpesa and perform necessary actions
#     # Example: Update the payment status in the database
#     return HttpResponse("Payment received. Thank you!")
# def payment(request):
#      return render(request,'select_payment.html')
# def bundle(request):
#      return render(request,'select_bundle.html')
# def payment_status(request):
#      return render(request,'payment_status.html')
