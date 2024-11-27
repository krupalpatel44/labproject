from django.db import models

# Create your models here.

class userregister(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    Address=models.TextField()


class blood(models.Model):
     created=models.DateTimeField(auto_now_add=True)
     name=models.CharField(max_length=20)
     email=models.EmailField()
     mobile=models.BigIntegerField()
     testname=models.CharField(max_length=50)
     gender=models.CharField(max_length=20)
     date=models.DateField()
     token_id=models.IntegerField()


class urine(models.Model):
     created=models.DateTimeField(auto_now_add=True)
     name=models.CharField(max_length=20)
     email=models.EmailField()
     mobile=models.BigIntegerField()
     testname=models.CharField(max_length=50)
     gender=models.CharField(max_length=20)
     date=models.DateField()
     token_id=models.IntegerField()

     
class xray(models.Model):
     created=models.DateTimeField(auto_now_add=True)
     name=models.CharField(max_length=20)
     email=models.EmailField()
     mobile=models.BigIntegerField()
     testname=models.CharField(max_length=50)
     gender=models.CharField(max_length=20)
     date=models.DateField()
     token_id=models.IntegerField()
     

class ultrasound(models.Model):
     created=models.DateTimeField(auto_now_add=True)
     name=models.CharField(max_length=20)
     email=models.EmailField()
     mobile=models.BigIntegerField()
     testname=models.CharField(max_length=50)
     gender=models.CharField(max_length=20)
     date=models.DateField()
     token_id=models.IntegerField()

     

class ctscan(models.Model):
     created=models.DateTimeField(auto_now_add=True)
     name=models.CharField(max_length=20)
     email=models.EmailField()
     mobile=models.BigIntegerField()
     testname=models.CharField(max_length=50)
     gender=models.CharField(max_length=20)
     date=models.DateField()
     token_id=models.IntegerField()


class Thayroid(models.Model):
     created=models.DateTimeField(auto_now_add=True)
     name=models.CharField(max_length=20)
     email=models.EmailField()
     mobile=models.BigIntegerField()
     testname=models.CharField(max_length=50)
     gender=models.CharField(max_length=20)
     date=models.DateField()
     token_id=models.IntegerField()


class Calcium(models.Model):
     created=models.DateTimeField(auto_now_add=True)
     name=models.CharField(max_length=20)
     email=models.EmailField()
     mobile=models.BigIntegerField()
     testname=models.CharField(max_length=50)
     gender=models.CharField(max_length=20)
     date=models.DateField()
     token_id=models.IntegerField()


class CRP(models.Model):
     created=models.DateTimeField(auto_now_add=True)
     name=models.CharField(max_length=20)
     email=models.EmailField()
     mobile=models.BigIntegerField()
     testname=models.CharField(max_length=50)
     gender=models.CharField(max_length=20)
     date=models.DateField()
     token_id=models.IntegerField()

class contact(models.Model):
     created=models.DateTimeField(auto_now_add=True)
     name=models.CharField(max_length=20)
     email=models.EmailField()
     msgg=models.CharField(max_length=500)





