from django.contrib import admin
from .models import *

# Register your models here.
class blooddata(admin.ModelAdmin):
    list_display=['name','email','mobile','testname','gender','date']

class urinedata(admin.ModelAdmin):
    list_display=['name','email','mobile','testname','gender','date']

class xraydata(admin.ModelAdmin):
    list_display=['name','email','mobile','testname','gender','date']

class ultrasounddata(admin.ModelAdmin):
    list_display=['name','email','mobile','testname','gender','date']

class thayroiddata(admin.ModelAdmin):
    list_display=['name','email','mobile','testname','gender','date']

class calciumdata(admin.ModelAdmin):
    list_display=['name','email','mobile','testname','gender','date']

class crpdata(admin.ModelAdmin):
    list_display=['name','email','mobile','testname','gender','date']

class userdata(admin.ModelAdmin):
    list_display=['firstname','city','Address']

class contactdata(admin.ModelAdmin):
    list_display=['name','email','msgg']


admin.site.register(userregister,userdata)
admin.site.register(blood,blooddata)
admin.site.register(urine,urinedata)
admin.site.register(xray,xraydata)
admin.site.register(ultrasound,ultrasounddata)
admin.site.register(Thayroid,thayroiddata)
admin.site.register(Calcium,calciumdata)
admin.site.register(CRP,crpdata)
admin.site.register(contact,contactdata)
