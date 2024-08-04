from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist

from .models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        email = request.POST['email']
        
        #check if user already exists
        try:
            user = User.objects.get(email=email)
            if user:
                return HttpResponse("User already exist. Try resetting your password")
        except ObjectDoesNotExist:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            phone = request.POST['phone']
            if len(phone) != 10:
                return HttpResponse("Provide a valid phone number")
            
            encrypted_pwd = make_password(request.POST['password'])
            user = User(first_name, last_name, email, phone, encrypted_pwd)
            user.save()

            return HttpResponse("register...")
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        plain_pwd = request.POST['password']
        
        try:
            user = User.objects.get(email=email)
            matched = check_password(plain_pwd, user.password)
            if matched:
                return HttpResponse("User logged in...")
            else:
                return HttpResponse("Incorrect password")
        except ObjectDoesNotExist:
            return HttpResponse("No such user")
    else:
        return render(request, 'login.html')