from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def user_signup(request):
    data={}
    if(request.method=="POST"):
        uname = request.POST['username']
        upassword = request.POST['password']
        cpassword = request.POST['cpassword']
        uemail = request.POST['email']
        print(uname, upassword, cpassword, uemail)
        if(uname == "" or upassword=="" or cpassword=="" or uemail==""):
            print("Hello")
            data['error_message'] = "fields cannot be empty"
            return render(request, "myapp/register.html", context=data)
        elif(upassword != cpassword):
            data['error_message'] = "Password is not same"
            return render(request, "myapp/register.html", context=data)
        elif(User.objects.filter(username=uname).exists()):
            data['error_message'] = uname+ " user name already exists"
            return render(request, "myapp/register.html", context=data)
        else:
            user = User.objects.create(username=uname, email=uemail)
            user.set_password(upassword)
            user.save()
            return redirect("/myapp/login")
    
    return render(request, "myapp/register.html")

def user_login(request):
    data={}
    if(request.method=="POST"):
        uname = request.POST['username']
        upassword = request.POST['password']

        if(uname == "" or upassword == ""):
            data['error_message'] = "fields can't be empty"
            return render(request, "myapp/login.html", context=data)
        elif(not User.objects.filter(username=uname).exists()):
            data["error_message"] = "Invalid username"
            return render(request, "myapp/login.html", context=data)
        else:
            user = authenticate(username=uname, password=upassword)
            if user is None:
                data["error_message"] = "wrong password"
                return render(request, "myapp/login.html", context=data)
            else:
                login(request, user)
                return redirect('/myapp/home')

    return render(request, "myapp/login.html")

def Home(request):
    data={}
    if(request.user.is_authenticated):
      user_id = request.user.id
      user= User.objects.get(id=user_id)
      data['username'] = user.username
    return render(request, "myapp/home.html", context=data)
 


    return render(request, "myapp/home.html")


def user_logout(request):
    logout(request)
    return redirect("/myapp/home")
