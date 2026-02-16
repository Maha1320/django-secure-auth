from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')

def signup_view(request):
    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not username or  not email or not password or not password2:
            messages.error(request, "Please fill all fields")
            return redirect('signup')
        
        if password != password2 :
            messages.error(request, "Passwords does not match")
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')


        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('signup')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Registration successfull Please login.")
        return redirect('login')
    
    return render(request, 'signup.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username").strip()
        password = request.POST.get("password").strip()

       
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username or password")
            return redirect("login")
        

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "login.html")


