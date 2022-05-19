from cgi import print_directory
from http.client import PRECONDITION_REQUIRED
from math import prod
import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from numpy import imag
from pygame import image
from .models import product, contactus, ispremium

# Create your views here.
def index(request):
    return render(request, "app_templates/Home.html")

def about(request):
    return render(request, "app_templates/About.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contactform = contactus(name=name, email=email, message=message)
        contactform.save()
    return render(request, "app_templates/contact.html")

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #checks
        if len(username) > 10:
            messages.error(request, "username must be of less than 10 charactors")
            return redirect('/handlesignup')
    
        if pass1 != pass2:
            messages.error(request, "passwords should match")
            return redirect('/handlesignup')

        #create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "your account has been created")
        return redirect('/handlesignup')
    return render(request, "app_templates/signup.html")

def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "logged in succesfully")
            return redirect('/')
        else:
            messages.error(request, "invalide credintials")
            return redirect('/')

    return render(request, "app_templates/login.html")

def handlelogout(request):
    logout(request)
    messages.success(request, "logged-out in succesfully")
    return redirect('/')

def uploadproduct(request):
    if request.method == "POST":
        title = request.POST.get('title')
        user = request.user
        description = request.POST.get('description')
        author = request.POST.get('author')
        pages = request.POST.get('pages')
        price = request.POST.get('price')
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        if len(request.FILES) != 0:
            image = request.FILES['image']
        
        prod = product(title=title,name=name, address=address, phone=phone,  author=author, price=price, pages=pages, description=description, image=image, user=user)
        prod.save()
        messages.success(request, "product uploaded successfully")
        return redirect('/')
        
    return render(request, "product_templates/uploadproduct.html")

def userprofile(request):
    user = request.user
    userproduct = product.objects.filter(user=user)
    print(userproduct)
    context = {'userproduct':userproduct}
    return render(request, "product_templates/userprofile.html", context)

def deleteproduct(request, pk):
    img = product.objects.filter(image=image)
    prod = product.objects.filter(prodid=pk)
    prod.delete()
    if len(img) > 0:
        os.remove(img)
    return redirect('/')

def productlist(request):
    producs_list = product.objects.all().reverse()
    context = {'list': producs_list}
    return render(request, "product_templates/productslist.html", context)

def productdetails(request, pk):
    prod_detail = product.objects.filter(prodid=pk)
    detail_context = {'detail':prod_detail}
    return render(request, "product_templates/productdetails.html", detail_context)
    
def search(request):
    query = request.GET['query']
    producttitle = product.objects.filter(title__icontains=query)
    holderaddress = product.objects.filter(address__icontains=query)
    finalprod = producttitle.union(holderaddress)
    
    return render(request, "product_templates/search.html", {'finalprod':finalprod})
    
def about(request):
    model = ispremium.objects.all()
    return render(request, "app_templates/about.html", {'model':model})
    
def pro(request):
    usermodel = ispremium.objects.filter(user=request.user)
    print(usermodel)
    
    return render(request, "app_templates/become_pro.html")

