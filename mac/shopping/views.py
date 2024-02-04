from django.shortcuts import render
from django.http import HttpResponse
from . models import Product,ContactUs,PlaceOrder,SlideData
from math import ceil
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def index(request):
    # products=Product.objects.all()
    # print(products)
    # n=len(products)
    # nslides=n//4 +ceil((n/4)-(n//4))
    # param={'no_of_slides':nslides,'range':range(1,nslides),'product':products }
    # allprods=[[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
    allprods=[]
    catprods=Product.objects.values('Catagory','id')
    cats={item['Catagory'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(Catagory=cat)
        n=len(prod)
        nslides=n//4 +ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nslides),nslides])  

    slidedata= SlideData.objects.all()   
    param={'allprods':allprods,'SlideData':slidedata} 
    return render(request,'shop/index.html',param)

def about(request):
    slide=Product.objects.all()
    return render(request,'shop/about.html',{'slides':slide,'range':range(1,4)})


def productview(request,myid):
    product=Product.objects.filter(id=myid)
    return render(request,'shop/productview.html',{'product':product[0]})

def login(request):
    return render(request,'shop/login.html',{})

def checkout(request):
    return render(request,'shop/checkout.html',{})

def signup_data(request):
    username=request.POST.get('username','default')
    email=request.POST.get('email','default')
    password=request.POST.get('password','default')
    user_exist=User.objects.filter(username=username)
    if user_exist:
        return HttpResponse("Username Or Email Already Exist,Please Either login with same userId or Email or Create new user")
    else:
        user=User.objects.create(username=username,email=email,password=password)
        user.set_password(password)
        user.save()
        return render(request,'shop/login.html',{})

def signin_data(request):
    if request.method=="POST":
        Username=request.POST['username']
        Password=request.POST['password']
        print(Username,Password)
        user=authenticate(username=Username,password=Password)

        if user is not None:
            login(request)
            return render(request,"shop/index.html",{})
        return HttpResponse("Invaild Username and Password or The Username already Exist")

def contact(request):
    if request.method=="POST":
        Fname=request.POST.get('First_name','default')
        Lname=request.POST.get('Last_name','default')
        email=request.POST.get('Email','default')
        phone=request.POST.get('Phone','default')
        Msg=request.POST.get('Msg','default')
        a=ContactUs(First_name=Fname,Last_name=Lname,Email=email,Phone=phone, Msg=Msg)
        a.save()
    return render(request,'shop/contact.html',{})

def Order(request):
    if request.method =='POST':
        items_json=request.POST.get("items_json",'default')
        Name=request.POST.get("Name",'default')
        Phone=request.POST.get("Phone",'default')
        Email=request.POST.get("Email",'default')
        Address=request.POST.get("Address",'default')
        
        City=request.POST.get("City",'default')
        State=request.POST.get("State",'default')
        ZipCode=request.POST.get("ZipCode",'default')

        order=PlaceOrder(items_json=items_json,Name=Name,Phone=Phone,Email=Email,Address=Address,City=City,State=State,ZipCode=ZipCode)
        order.save()
        thank=True
        return render(request,"shop/checkout.html",{'thank':thank})
    return render(request,"shop/checkout.html",{})