from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from dairyapp.models import DairyEntry
# Create your views here.

def home(request):
    return render(request, "home.html")


def user_register(request):
    if(request.method=="POST"):
        data={}
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword= request.POST['cpassword']

        print(name, password, email, cpassword)
        if(name=="" or email==""or password==""or cpassword==""):
            data['error_msg'] = "Fields can't be empty"
            return render(request, "register.html", context=data)
        
        elif(password != cpassword):
         data['error_msg'] = "Password did not match"
         return render(request, 'register.html', context=data)
        
        elif(User.objects.filter(username=name).exists()):
         data['error_msg'] = name+" username already exists"
         return render(request, 'register.html', context=data)
        else:
         user = User.objects.create(username=name)
         user.set_password(password)
         user.save()
         return redirect("/login")


            
    return render(request, "register.html")

def user_login(request):
    data={}
    if(request.method=="POST"):
      name=request.POST['username']
      password=request.POST['password']
      # print(username,password,cpassowrd)
      if(name=="" or password==""):
         # print("fields cant be empty")
         data['error_msg']="fields cant be empty"
         return render(request,'login.html',context=data)
      elif(not User.objects.filter(username=name).exists()):
         # print(uname + " is already exist")
         data['error_msg']=name + " is does not exist"
         return render(request,'login.html',context=data)
      else:
         user=authenticate(username=name, password=password)
         if user is None:
            data['error_msg']="Wrong password"
            return render(request, "login.html", context=data)
         else:
            login(request, user)
            return redirect('/home')
    return render(request, "login.html")


def add_entry(request):
   if(request.method=="POST"):
      data={}
      title = request.POST['title']
      content = request.POST['content']

      print(title)
      print(content)

      if(title=="" or content==""):
        data['error_msg']="Please add Title and Content"
        print("fields can't be empty")
        return render(request, "addEntry.html", context=data)
      else:
         added_entry = DairyEntry.objects.create(title=title, content=content)
         added_entry.save()
         return redirect('/home')
   return render(request, "addEntry.html")

def show_entry(request):
    if(request.user.is_authenticated):
        data = {}
        entries = DairyEntry.objects.all()
        data['entries'] = entries
        return render(request, "dairy.html", context=data)
        
    else:
        return redirect("/")

        
