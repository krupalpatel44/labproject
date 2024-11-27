from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index),
    path('login/',views.login,name='login'),
    path('register/',views.register),
    path('test/',views.test,name='test'),
    path('about/',views.about),
    path('userlogout/',views.userlogout),
    path('otpverify/',views.otpverify,name='otpverify'),
    path('bloodtest/',views.bloodtest),
    path('urintest/',views.urintest),
    path('xray/',views.xray),
    path('ultrasound/',views.ultrasound),
    path('ctscan/',views.ctscan),
    path('thairoid/',views.thairoid),
    path('calcium/',views.calcium),
    path('protin/',views.protin),
    path('contact/',views.contact),
    path('updateprofile/',views.updateprofile),
    path('resetpass/',views.resetpass,name='resetpass'),
    path('emailverify/',views.emailverify),

]