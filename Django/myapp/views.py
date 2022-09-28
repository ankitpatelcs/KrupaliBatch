from django.shortcuts import render,redirect
from django.http import JsonResponse
from myapp.models import *
from seller.models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        try:
            userobj = User.objects.get(email=request.POST['email'])
            if request.POST['pass'] == userobj.password:
                request.session['email']=request.POST['email']
                request.session['name']=userobj.name
                return redirect('index')
        except:
            return render(request,'login.html',{'msg':'Email Not Registered'})

    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        if request.POST['pass']==request.POST['cnfpass']:
            User.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                password=request.POST['pass']
            )
            return render(request,'login.html')
        else:
            return render(request,'register.html',{'msg':'Passwords did not match.!'})
    return render(request,'register.html')

def contact(request):
    return render(request,'contact.html')

def products(request):
    plist = Product.objects.all()
    for item in plist:
        item.discountedprice=item.price-(item.price*item.discount/100)

    return render(request,'products.html',{'productlist':plist})

def single(request,pid):
    pobj = Product.objects.get(id=pid)
    pobj.discountedprice=pobj.price-(pobj.price*pobj.discount/100)
    return render(request,'single.html',{'pobj':pobj})

def addtocart(request):
    pid=request.GET['pid']
    userobj = User.objects.get(email=request.session['email'])
    pobj = Product.objects.get(id=pid)

    Cart.objects.create(
        product=pobj,
        user=userobj,
        quantity=1
    )
    return JsonResponse({'msg':'Employee Added'})