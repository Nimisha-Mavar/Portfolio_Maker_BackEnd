from Portfolio_Maker.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
from django.shortcuts import render, HttpResponse,redirect
import razorpay
from payment.models import Payment
from django.conf import settings
from Templates.models import *
from Services.models import Portfolio,Resume
#for Ready page
client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY))
def Ready_page(request):
    cat=request.POST['cat']
    idd=request.POST['id']
    if cat == 'Portfolio':
        pdata=Portfolio.objects.get(Portfolio_id=idd)
        tid=pdata.Template_id
        temp=Detail.objects.get(id=tid)
        ttype=temp.Temp_type
        data={
                'pid':idd,
                'tname':temp.Temp_name
            }
        if ttype == 'Premium':
            if Payment.objects.filter(Portfolio_id=idd).exists():
                return render(request,'Temp_ready.html',data)
            else:
                Total=temp.Temp_price-(temp.Temp_price*temp.offer()/100)
                Payment.Temp_price = Total*100
                order_currency = 'INR'
                payment_order= client.order.create({'amount':Payment.Temp_price, 'currency':order_currency, 'payment_capture': 1})
                Payment.razor_pay_order_id = payment_order['id']
                context = {
                    'pid':idd,
                    'temp':temp,
                    'total':Total,
                    'amount' : 500, 
                    'api_key':RAZORPAY_API_KEY, 
                    'payment_order': payment_order,
                    'order_id': Payment.razor_pay_order_id
                }
                return render(request,'Invoice.html',context)
        else:
            return render(request,'Temp_ready.html',data)
    else:
        return HttpResponse("Resume")
# Create your views here.

#client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY))
"""def payment(request):
    pid=request.POST['pid']
    Payment.Temp_price = 400*100
    order_currency = 'INR'
    payment_order= client.order.create({'amount':Payment.Temp_price, 'currency':order_currency, 'payment_capture': 1})

    Payment.razor_pay_order_id = payment_order['id']
    
    context = {
        'amount' : 500, 
        'api_key':RAZORPAY_API_KEY, 
        'payment_order': payment_order,
        'order_id': Payment.razor_pay_order_id
    }
    return render(request,'Payment.html',context)"""

def success(request):
    order_id = request.GET.get('order_id')
    total=request.GET.get('total')
    pid=request.GET.get('pid')
    pay = Payment(razor_pay_order_id = order_id)
    pay.is_paid = True
    pay.Total=total
    pay.Portfolio_id=pid
    pay.save()
    pdata=Portfolio.objects.get(Portfolio_id=pid)
    tid=pdata.Template_id
    temp=Detail.objects.get(id=tid)
    data={
        'pid':pid,
        'tname':temp.Temp_name
    }
    return render(request,'Temp_ready.html',data)