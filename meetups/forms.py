from django import forms

#from .models import Participant

# USeful when we are using the save method the views class
# class RegistrationForm(forms.ModelForm):
    
#     class Meta:
#         model = Participant
#         fields = ['email']

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your Email')