from django.shortcuts import render,redirect
from .models import Users
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages


def User_register(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
       
        user = Users(full_name = fullname,email = email,username = username ,password = make_password(password))
        user.save()
        return redirect('login')
        
    return render(request,'register.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
    
        user = Users.objects.filter(username = username).first()

        if not user:
            messages.error(request,"Invalid Username")
            return redirect('login',permanent=True)
        
        elif not check_password(password,user.password):
            messages.error(request,"Invalid Password")
            return redirect('login',permanent=True)
        
        else:
            return redirect('play_music')

    return render(request,'login.html')