from django.shortcuts import render
from userSignup import models
from django.http import HttpResponse
# Create your views here.

def signUp(request):
    if (request.method == "POST"):
        uname = request.POST['user_name']
        uemail = request.POST['user_email']
        upassword = request.POST['user_password']
        uconfirmpassword = request.POST['confirm_password']

        print(uname,uemail,upassword,uconfirmpassword)
        
        if( models.UserSignUpModel.objects.filter(user_email=uemail).exists()):
            # return HttpResponse("Email already exists. Login instead")
            return render(request, 'signup/already.html')
        
        if(upassword != uconfirmpassword):
            print(f"The {upassword} is not same {uconfirmpassword}")
            return HttpResponse("Please check your password")
        else:
            print("Password different")
            hashpassword =  hash(upassword)
            hashconpassword = hash(uconfirmpassword)
            print(hashpassword, hashconpassword)
            user_data = models.UserSignUpModel.objects.create(user_name=uname, user_email=uemail, user_password=hashpassword, confirm_password=hashconpassword)
            return HttpResponse("Sign up Sucessful")
    return render(request, "signup/signup.html")


def userLogin(request):
    
     return render(request, "login/login.html")