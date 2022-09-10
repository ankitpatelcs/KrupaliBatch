from urllib import request
from django.shortcuts import render,redirect

import seller
from seller.models import Seller

# Create your views here.

def seller_login(request):
    if request.method=='POST':
        try:
            sellerobj = Seller.objects.get(email=request.POST['email'])
            if request.POST['password'] == sellerobj.password:
                request.session['email']=request.POST['email']
                request.session['name']=sellerobj.name
                return render(request,'seller-index.html')
            else:
                return render(request,'seller-login.html',{'msg':'wrong password'})
        except:
            return render(request,'seller-login.html',{'msg':'Email Not Found'})
    return render(request,'seller-login.html')

def seller_index(request):
    return redirect(request,'seller-index.html')