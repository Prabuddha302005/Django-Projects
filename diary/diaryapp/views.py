from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from diaryapp.models import DairyEntry

# Create your views here.
def homepage(request):
    return render(request, "home.html")


def user_register(request):
    data={}
    if(request.method=="POST"):
        uname = request.POST['username']
        upass = request.POST['password']
        cpass = request.POST['cpassword']
        print(uname, upass)
        
        if(uname=="" or upass=="" or cpass==""):
         data['error_msg'] = "fields cannot be empty"
         return render(request, 'register.html', context=data)
        elif(upass != cpass):
         data['error_msg'] = "Password did not match"
         return render(request, 'register.html', context=data)
        elif(User.objects.filter(username=uname).exists()):
         data['error_msg'] = uname+" username already exists"
         return render(request, 'register.html', context=data)
        else:
         user = User.objects.create(username=uname)
         user.set_password(upass)
         user.save()
         return redirect("/login")

    return render(request, "register.html")


def user_login(request):
   data={}
   if(request.method=="POST"):
      uname=request.POST['username']
      upass=request.POST['password']
      # print(username,password,cpassowrd)
      if(uname=="" or upass==""):
         # print("fields cant be empty")
         data['error_msg']="fields cant be empty"
         return render(request,'login.html',context=data)
      elif(not User.objects.filter(username=uname).exists()):
         # print(uname + " is already exist")
         data['error_msg']=uname + " is does not exist"
         return render(request,'login.html',context=data)
      else:
         user=authenticate(username=uname, password=upass)
         if user is None:
            data['error_msg']="Wrong password"
            return render(request, "login.html", context=data)
         else:
            login(request, user)
            return redirect('/show-entry')
   return render(request, "login.html")

def user_logout(request):
   logout(request)
   return redirect("/")

def add_entry(request):
   data={}
   if(request.method=="POST"):
      title=request.POST['title']
      content=request.POST['content']
      print(title, content)

      if(title=="" or content==""):
         data['error_msg'] = "Please enter title and content"
         return render(request, "add_entry.html", context=data)
      else:
         user_id = request.user.id;
         user = User.objects.get(id=user_id)
         save_entry = DairyEntry.objects.create(title=title, content=content, uid=user)
         save_entry.save()
         return redirect("/show-entry")
   return render(request, "add_entry.html")


def show_entry(request):
   data={}
   if(request.user.is_authenticated):
    show_entries = DairyEntry.objects.filter(uid=request.user.id)
    data['entry'] = show_entries
    return render(request, "show_entry.html", context=data)
   
def delete_entry(request, entry_id):
   delete_entry = DairyEntry.objects.get(id=entry_id)
   delete_entry.delete()
   return redirect("/show-entry")
   
def update_entry(request, entry_id):
   data={}
   entry = DairyEntry.objects.filter(id=entry_id)
   data['entry'] = entry[0]
   if(request.method=="POST"):
      title=request.POST['title']
      content=request.POST['content']
      print(title, content)

      if(title=="" or content==""):
         data['error_msg'] = "Please enter title and content"
         return render(request, "add_entry.html", context=data)
      else:
         entry = DairyEntry.objects.filter(id=entry_id)
         entry.update(title=title, content=content)
         return redirect("/show-entry")
   return render(request, "update_entry.html", context=data)
   