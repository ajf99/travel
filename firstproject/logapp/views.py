from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalied login')
            return redirect('login')
    return render(request,'login.html')
def registration(request):
    if request.method== 'POST':
        u=request.POST['user_name']
        fn = request.POST['First_name']
        sn = request.POST['Second_name']
        eid= request.POST['Email']
        ps = request.POST['password']
        cps = request.POST['password1']
        if ps==cps:
            if User.objects.filter(username=u).exists():
                messages.info(request,'username taken')
                return redirect('registration')
            elif User.objects.filter(email=eid).exists():
                messages.info(request,'email taken')
                return redirect('registration')
            else:
                user=User.objects.create_user(username=u,password=ps,first_name=fn,last_name=sn,email=eid)

                user.save();
                return redirect('login')


        else:
            messages.info(request,'password not matching')
            return redirect('registration')
        return redirect('/')

    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')