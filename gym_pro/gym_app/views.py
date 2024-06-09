from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from gym_app.models import Contact,MembershipPlan,Trainer
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


def contact(request):
    if request.method=="POST":
        username=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        description=request.POST.get('desc')
        myuser=Contact(name=username,email=email,phonenumber=number,description=description)
        myuser.save()
        messages.info(request,"Thank you for contacting us")
        return redirect("/contact")
    return render(request,"contact.html")



def handleEnroll(request):
    Membership=MembershipPlan.objects.all()
    trainer=Trainer.objects.all()
    context={"Membership":Membership,"SelectTrainer":trainer}
    return render(request,"enroll.html",context)