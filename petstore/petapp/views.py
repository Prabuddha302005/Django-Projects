from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from petapp import models
# Create your views here.
def index_page(request):
    return render(request, "indexpage/index.html")

def user_register(request):
    data={}
    if(request.method == "POST"):
        uname = request.POST['username']
        uemail = request.POST['email']
        upassword = request.POST['password']
        cupassword = request.POST['cpassword']
        print(uname, uemail, upassword)

        if(uname == "" or uemail == "" or upassword==""):
            data['error_msg'] = "Fields can't be empty"
            return render(request, "register/signup.html", context=data)
        elif(upassword != cupassword):
            data['error_msg'] = "Password is not same"
            return render(request, "register/signup.html", context=data)
        elif(User.objects.filter(username=uname).exists()):
            data['error_msg'] = "username already exists"
            return render(request, "register/signup.html", context=data)
        else:
            user = User.objects.create(username=uname, email=uemail)
            user.set_password(upassword)
            user.save()
            return redirect("/login")
    return render(request, "register/signup.html")  


def user_login(request):
    data={}
    if(request.method == "POST"):
        uname = request.POST['username']
        upassword = request.POST['password']

        print(uname, upassword)

        if(uname == "" or upassword==""):
            data['error_msg'] = "Fields can't be empty"
            return render(request, "login/login.html", context=data)
        if(not User.objects.filter(username=uname).exists()):
            data['error_msg'] = "Username not found"
            return render(request, "login/login.html", context=data)    
        else:
            user = authenticate(username=uname, password=upassword)
            if user is None:
                data['error_msg'] = "Wrong password"
                return render(request, 'login/login.html', context=data) 
            else:
                login(request, user)
                # return HttpResponse("Login working sucessfull")
                
                return redirect('/home')   
    return render(request, "login/login.html")  

def user_home(request):
    data={}
    if(request.user.is_authenticated):
    
      user_id=request.user.id
      user=User.objects.get(id=user_id)
      data['username']=user.username
    
      pets = models.MyPetModel.objects.all()
      data['mypet'] = pets
      return render(request, "home/home.html", context=data)
    else:
      pets = models.MyPetModel.objects.all()
      data['mypet'] = pets
      return render(request, "home/home.html", context=data)


      





    
    
    
    return render(request, "home/home.html", context=data)
  

def user_logout(request):
   logout(request)
   return redirect('/home')

