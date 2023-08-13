import requests
import base64
import json
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from .models import Transaction
from .generateAccesstoken import get_access_token

def initiate_payment(request):
    if request.method == 'POST':
        item = request.POST.get('item')
        amount = request.POST.get('amount')
        phone_number = request.POST.get('phone_number')

        access_token_response = get_access_token(request)
        if isinstance(access_token_response, JsonResponse):
            access_token = access_token_response.content.decode('utf-8')
            access_token_json = json.loads(access_token)
            access_token = access_token_json.get('access_token')
            if access_token:
                business_short_code = '174379'
                passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
                callback_url = 'https://api.github.com/'
                reference = 'Twizard Software'
                timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                password = base64.b64encode((business_short_code + passkey + timestamp).encode()).decode()
                party_a = phone_number


                stk_push_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
                stk_push_headers = {
                    'Authorization': 'Bearer ' + access_token,
                    'Content-Type': 'application/json'
                }

                stk_push_payload = {
                    'BusinessShortCode': business_short_code,
                    'Password': password,
                    'Timestamp': timestamp,
                    'TransactionType': 'CustomerPayBillOnline',
                    'Amount': amount,
                    'PartyA': party_a,
                    'PartyB': business_short_code,
                    'PhoneNumber': party_a,
                    'CallBackURL': callback_url,
                    'AccountReference': reference,
                    'TransactionDesc': f'Payment for {item}'
                }

                try:
                    response = requests.post(stk_push_url, headers=stk_push_headers, json=stk_push_payload)
                    response.raise_for_status()
                    response_data = response.json()
                    checkout_request_id = response_data['CheckoutRequestID']
                    response_code = response_data['ResponseCode']

                    if response_code == "0":
                        Transaction.objects.create(item=item, amount=amount, phone_number=phone_number)
                        return JsonResponse({'CheckoutRequestID': checkout_request_id, 'ResponseCode': response_code})
                    else:
                        return JsonResponse({'error': 'STK push failed.'})
                except requests.exceptions.RequestException as e:
                    return JsonResponse({'error': str(e)})
            else:
                return JsonResponse({'error': 'Access token not found.'})
        else:
            return JsonResponse({'error': 'Failed to retrieve access token.'})
    else:
        return render(request, 'payment.html', {'items': ['Item 1', 'Item 2', 'Item 3']})
