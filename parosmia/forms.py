from django import forms
from .models import LogMessage, Person, Experience
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ['message',]   # NOTE: the trailing comma is required

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['log_date','type','quantity','description','rating','smells_like',]   # NOTE: the trailing comma is required


class Login(forms.Form):
#    class Meta:
#        model = Person
#        fields = ['email', 'password',]
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class DateInput(forms.DateInput):
    input_type = 'date'
    
class Register(UserCreationForm):
    class Meta:
        model = User
        
        fields = ['first_name', 'last_name', 'username', 'email',]
        labels = {'first_name': "First Name", 'last_name': "Last Name", 'username': "Username", 'email' : "Email", 'password' : "Password"}
        #widgets = {'dob': DateInput(),}


