from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
import random
from finalproject import settings
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    user=request.session.get('user')
    return render(request,'index.html',{'user':user})

def login(request):
    msg=''
    if request.method=="POST":
        unm=request.POST['username']
        upass=request.POST['password']
        user=userregister.objects.filter(username=unm,password=upass)
        uid=userregister.objects.get(username=unm)
        if user:
            print("Login Successfully...")
            msg="LOGIN SUCCESS..."
            request.session['user']=unm
            request.session['userid']=uid.id
            return redirect('/')
        else:
            print("login failed!!!")
            msg="LOGIN FAILED!!!"

    return render(request,'login.html',{'msg':msg})

def register(request):
    msg=''
    global newuser
    if request.method=='POST':
        newuser=registerform(request.POST)
        username=''
        if newuser.is_valid():
            username=newuser.cleaned_data.get('username')
            try:
                userregister.objects.get(username=username)
                print("Username Is Allready Exists....")
            except userregister.DoesNotExist:
                print("Register Successfully!!!")
                msg='register success...'
                
                # email 
                global otp
                otp=random.randint(11111,99999)
                nm=request.POST['firstname']
                sub='Your One Time Password '
                msg=f'Welcome {nm}\n\n Your Otp Is {otp}\n\n Congratulations Your Registration Is Successfull.\n\n Thank You For Visit Our Diagnostic Lab Website.\n\n\n Shree Diagnostic Lab\n 9313819231\n Jasdan-Rajkot.'
                from_id=settings.EMAIL_HOST_USER
                to_id=[request.POST['username']]
                send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)
                return redirect('otpverify')
               
        else:
            print(newuser.errors)  

    return render(request,'register.html',{'msg':msg}) 

def test(request):
    user=request.session.get('user')
    global token
    token=tokenid()
    print(token)
    return render(request,'test.html',{'user':user})

def about(request):
    user=request.session.get('user')
    return render(request,'about.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')

def otpverify(request):
    msg=''
    global otp
    
    print("OTP:",otp)
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            newuser.save()
            print('verification successfully.')
            msg='your otp is correct'
            return redirect('login')
        else:
            print('not success')
            msg='SORRY...YOUR OTP IS WRONG!!!'

    return render(request,'otpverify.html',{'msg':msg})
 
def bloodtest(request):
    global token
    token=tokenid()
    msg=''
    if request.method=='POST':
        bf=bloodform(request.POST)
        if bf.is_valid():
            bf.save()
            msg='Your Appoinment IS Suceess...'
            print("data Saved...")

            #email
            nm=request.POST['email']
            tn=request.POST['testname']
            sub='Congratulations!!!'
            msg=f'Your {tn} Appoinment Has Been Successfully Booked.\n\n This is Your Appoinment Token Id: {token}.\n\n Thank You For Visit Our Diagnostic Lab Website.\n\n\n Shree Diagnostic Lab\n 9313819231\n Jasdan-Rajkot.'
            from_id=settings.EMAIL_HOST_USER
            to_id=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)
            return redirect('/')
                   
        else:
            print(bf.errors)
            msg='ERROR..!! Try Again..'
        
    return render(request,'bloodtest.html',{'msg':msg,'token':token})

def urintest(request):
    global token
    token=tokenid()
    msg=''
    if request.method=='POST':
        uf=urineform(request.POST)
        if uf.is_valid():
            uf.save()
            msg='Your Appoinment IS Suceess...'
            print("data Saved...")

            #email
            nm=request.POST['email']
            tn=request.POST['testname']
            sub='Congratulations!!!'
            msg=f'Your {tn} Appoinment Has Been Successfully Booked.\n\n This is Your Appoinment Token Id: {token}.\n\n Thank You For Visit Our Diagnostic Lab Website.\n\n\n Shree Diagnostic Lab\n 9313819231\n Jasdan-Rajkot.'
            from_id=settings.EMAIL_HOST_USER
            to_id=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)
            return redirect('/')
        else:
            print(uf.errors)
            msg='ERROR..!! Try Again..'
        
    return render(request,'urintest.html',{'msg':msg, "token":token})

def xray(request):
    global token
    token=tokenid()
    msg=''
    if request.method=='POST':
        xf=xrayform(request.POST)
        if xf.is_valid():
            xf.save()
            msg='Your Appoinment IS Suceess...'
            print("data Saved...")

          #email
            nm=request.POST['email']
            tn=request.POST['testname']
            sub='Congratulations!!!'
            msg=f'Your {tn} Appoinment Has Been Successfully Booked.\n\n This is Your Appoinment Token Id: {token}.\n\n Thank You For Visit Our Diagnostic Lab Website.\n\n\n Shree Diagnostic Lab\n 9313819231\n Jasdan-Rajkot.'
            from_id=settings.EMAIL_HOST_USER
            to_id=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)
            return redirect('/')
        else:
            print(xf.errors)
            msg='ERROR..!! Try Again..'
        
    return render(request,'xray.html',{'msg':msg,"token":token})

def ultrasound(request):
    global token
    token=tokenid()
    msg=''
    if request.method=='POST':
        uf=ultrasoundform(request.POST)
        if uf.is_valid():
            uf.save()
            msg='Your Appoinment IS Suceess...'
            print("data Saved...")

        #email
            nm=request.POST['email']
            tn=request.POST['testname']
            sub='Congratulations!!!'
            msg=f'Your {tn} Appoinment Has Been Successfully Booked.\n\n This is Your Appoinment Token Id: {token}.\n\n Thank You For Visit Our Diagnostic Lab Website.\n\n\n Shree Diagnostic Lab\n 9313819231\n Jasdan-Rajkot.'
            from_id=settings.EMAIL_HOST_USER
            to_id=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)
            return redirect('/')
        else:
            print(uf.errors)
            msg='ERROR..!! Try Again..'
        
    return render(request,'ultrasound.html',{'msg':msg,"token":token})

def ctscan(request):
    global token
    token=tokenid()
    msg=''
    if request.method=='POST':
        cf=ctscanform(request.POST)
        if cf.is_valid():
            cf.save()
            msg='Your Appoinment IS Suceess...'
            print("data Saved...")

        #email
            nm=request.POST['email']
            tn=request.POST['testname']
            sub='Congratulations!!!'
            msg=f'Your {tn} Appoinment Has Been Successfully Booked.\n\n This is Your Appoinment Token Id: {token}.\n\n Thank You For Visit Our Diagnostic Lab Website.\n\n\n Shree Diagnostic Lab\n 9313819231\n Jasdan-Rajkot.'
            from_id=settings.EMAIL_HOST_USER
            to_id=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)
            return redirect('/')
        else:
            print(cf.errors)
            msg='ERROR..!! Try Again..'
        
    return render(request,'ctscan.html',{'msg':msg,"token":token})

def thairoid(request):
    global token
    token=tokenid()
    msg=''
    if request.method=='POST':
        tf=Thayroidform(request.POST)
        if tf.is_valid():
            tf.save()
            msg='Your Appoinment Is Suceess...'
            print("data Saved...")

        #email
            nm=request.POST['email']
            tn=request.POST['testname']
            sub='Congratulations!!!'
            msg=f'Your {tn} Appoinment Has Been Successfully Booked.\n\n This is Your Appoinment Token Id: {token}.\n\n Thank You For Visit Our Diagnostic Lab Website.\n\n\n Shree Diagnostic Lab\n 9313819231\n Jasdan-Rajkot.'
            from_id=settings.EMAIL_HOST_USER
            to_id=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)
            return redirect('/')
        else:
            print(tf.errors)
            msg='ERROR..!! Try Again..'
        
    return render(request,'thairoid.html',{'msg':msg,"token":token})

def calcium(request):
    global token
    token=tokenid()
    msg=''
    if request.method=='POST':
        calf=Calciumform(request.POST)
        if calf.is_valid():
            calf.save()
            msg='Your Appoinment IS Suceess...'
            print("data Saved...")

        #email
            nm=request.POST['email']
            tn=request.POST['testname']
            sub='Congratulations!!!'
            msg=f'Your {tn} Appoinment Has Been Successfully Booked.\n\n This is Your Appoinment Token Id: {token}.\n\n Thank You For Visit Our Diagnostic Lab Website.\n\n\n Shree Diagnostic Lab\n 9313819231\n Jasdan-Rajkot.'
            from_id=settings.EMAIL_HOST_USER
            to_id=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)
            return redirect('/')
        else:
            print(calf.errors)
            msg='ERROR..!! Try Again..'
        
    return render(request,'calcium.html',{'msg':msg,"token":token})

def protin(request):
    global token
    token=tokenid()
    msg=''
    if request.method=='POST':
        pf=CRPform(request.POST)
        if pf.is_valid():
            pf.save()
            msg='Your Appoinment IS Suceess...'
            print("data Saved...")

        #email
            nm=request.POST['email']
            tn=request.POST['testname']
            sub='Congratulations!!!'
            msg=f'Your {tn} Appoinment Has Been Successfully Booked.\n\n This is Your Appoinment Token Id: {token}.\n\n Thank You For Visit Our Diagnostic Lab Website.\n\n\n Shree Diagnostic Lab\n 9313819231\n Jasdan-Rajkot.'
            from_id=settings.EMAIL_HOST_USER
            to_id=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id) 
            return redirect('/')
        else:
            print(pf.errors)
            msg='ERROR..!! Try Again..'
        
    return render(request,'protin.html',{'msg':msg,"token":token})

def contact(request):
    msg=''
    user=request.session.get('user')
    if request.method=='POST':
        conf=contactform(request.POST)
        if conf.is_valid():
            conf.save()
            msg='Your Message Is Suceessfully Sending...'
            print("data Saved...")
            return redirect('/')
        else:
            print(conf.errors)
            msg='ERROR..!! Try Again..'
    return render(request,'contact.html',{'msg':msg,'user':user})


def updateprofile(request):
    msg=''
    user=request.session.get('user')
    userid=request.session.get('userid')
    cid=userregister.objects.get(id=userid)
    print(cid)
    if request.method=="POST":
       uform=updateform(request.POST)
       if uform.is_valid():
           uform=updateform(request.POST,instance=cid)
           uform.save()
           print('Your Profile Has Been Updated!')
           msg='Your Profile Has Been Updated!'

           #email
           nm=request.POST['firstname']
           sub='Your Profile Has Been Updated... '
           msg=f'Congratulations Your Profile Updateded Successfully.\n\n Thank You For Visit Our Diagnostic Lab Website.\n\n\n Shree Diagnostic Lab\n 9313819231\n Jasdan-Rajkot.'
           from_id=settings.EMAIL_HOST_USER
           to_id=[request.POST['username']]
           send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)
           return redirect('/')
       else:
           msg='Error..!Try Again!'
           print(uform.errors)
    return render(request,'updateprofile.html',{'user':user,'msg':msg,'cid':cid})


def resetpass(request):
    if request.method=='POST':
        newpass=passform(request.POST)
        uid=request.session.get('uid')
        cid=userregister.objects.get(id=uid)
        if newpass.is_valid():
            newpass=passform(request.POST,instance=cid)
            newpass.save()
            print('Password Reset Successfully')
            return redirect('login')
        else:
            print(newpass.errors)

    return render(request,'resetpass.html')

def emailverify(request):
    if request.method=='POST':
        email=request.POST['email']
        umail=userregister.objects.get(username=email)
        request.session['uid']=umail.id
        return redirect('resetpass')
    else:
        print('Error...')
    return render(request,'emailverify.html')

def tokenid():
    global token
    token=random.randint(1111,9999)
    return token


