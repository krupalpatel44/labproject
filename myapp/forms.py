from django import forms
from .models import *

class registerform(forms.ModelForm):
    class Meta:
        model=userregister
        fields='__all__'


class bloodform(forms.ModelForm):
    class Meta:
        model=blood
        fields='__all__'

class urineform(forms.ModelForm):
    class Meta:
        model=urine
        fields='__all__'

class xrayform(forms.ModelForm):
    class Meta:
        model=xray
        fields='__all__'

class ultrasoundform(forms.ModelForm):
    class Meta:
        model=ultrasound
        fields='__all__'

class ctscanform(forms.ModelForm):
    class Meta:
        model=ctscan
        fields='__all__'

class Thayroidform(forms.ModelForm):
    class Meta:
        model=Thayroid
        fields='__all__'

class Calciumform(forms.ModelForm):
    class Meta:
        model=Calcium
        fields='__all__'

class CRPform(forms.ModelForm):
    class Meta:
        model=CRP
        fields='__all__'       

class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'   

class updateform(forms.ModelForm):
    class Meta:
        model=userregister
        fields=['firstname','username','password','city','Address']

class passform(forms.ModelForm):
    class Meta:
        model=userregister
        fields=['password']