from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
#add here some logic
# Create your views here.

def Home(request):
    return render(request,"index.html",)


def signup(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
        try:

            if len(username)>10 or len(username)<10:
                messages.info(request,"phone number must be 10 digit")
                return redirect('/signup')
        except Exception as identifier:
            pass
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Username is Taken")
                return redirect("/signup")
        except Exception as identifier:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request,"email is Taken")
                return redirect("/signup")
        except Exception as identifier:
            pass

        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"User is created Please Login")
        return redirect("/login")

    return render (request,"signup.html")


def handlelogin(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        pass1=request.POST.get("pass1")
        print(username,pass1)
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            messages.success(request,"Login successfully")
            return redirect("/")
        else:
            messages.error(request,"Invalid Credentials")            
    return render (request,"login.html")


def logout_user(request):
    logout(request)
    messages.success(request,"Logout User")
    return redirect ('/login')
