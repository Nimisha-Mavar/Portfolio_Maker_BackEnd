from Portfolio_Maker.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
from django.shortcuts import render, HttpResponse
import razorpay
from payment.models import Payment
from django.conf import settings


# Create your views here.

client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY))
def Payment1(request):
    Payment.Temp_price = 400
    order_currency = 'INR'

    payment_order= client.order.create({'amount':Payment.Temp_price, 'currency':order_currency, 'payment_capture': 1})

    Payment.razor_pay_order_id = payment_order['id']
    
    context = {
        'amount' : 500, 'api_key':RAZORPAY_API_KEY, 'payment_order': payment_order
    }
    
    return render(request, 'Invoice.html', context)

def success(request):
    order_id = request.GET.get('order_id')
    pay = Payment(razor_pay_order_id = order_id)
    pay.is_paid = True
    pay.save()
    data={
        
    }
    return HttpResponse('payment Successfull')