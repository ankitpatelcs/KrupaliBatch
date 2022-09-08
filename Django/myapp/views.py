from django.shortcuts import render,redirect

from myapp.models import User

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