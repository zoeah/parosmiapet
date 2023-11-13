import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from parosmia.forms import LogMessageForm, Login, Register, ExperienceForm
from parosmia.models import LogMessage, Person, Experience
from django.views import generic
from django.contrib.humanize.templatetags import humanize
from django.views.generic import ListView, View
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.db.models import Prefetch, Count
from django.contrib.auth.models import User
from django.contrib.auth import logout


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "parosmia/about.html")

def track(request):
    form = ExperienceForm(request.POST or None)
    model = Experience
    Experiences = Experience.objects.filter(user=request.user).order_by('-log_date').values
    #Experiences = Experience.objects.filter(user=request.user).order_by('-log_date').values
    if request.method == "POST":
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()
            form = ExperienceForm
            return render(request, "parosmia/track.html", {"form": form,'Experience_list':Experiences})
        else:
            messages.success(request, 'You have signed up successfully.')
            return render(request, "parosmia/track.html", {"form": form,'Experience_list':Experiences})
    else:
        form = ExperienceForm
        return render(request, "parosmia/track.html",{'form': form,'Experience_list':Experiences})
    

def home(request):
     return render(request, "parosmia/home.html", {'myperson': request.user})

def logout(request):
    logout(request)

def resources(request):
    return render(request, "parosmia/resources.html")

def auth(request):
    if request.method == 'GET':
        form = Login()
        return render(request, "parosmia/login.html", {'form': form})
    if request.method == 'POST':
        form = Login(request.POST) 
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)            
                messages.success(request, 'You have signed in successfully.')
                return redirect("/home")
            else:               
                return render(request, 'parosmia/login.html', {'form': form})
        else:
            return render(request, 'parosmia/login.html', {'form': form})

def register(request):
    if request.method == 'GET':
        form = Register()
        return render(request, 'parosmia/register.html', {'form': form})    
    if request.method == 'POST':
        form = Register(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'You have signed up successfully.')
            login(request,user)
            return redirect('/home')
        else:
            return render(request, 'parosmia/register.html', {'form': form})

def welcome(request):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'parosmia/welcome.html',
        {
            'date': datetime.now(),
        }
    )
    
def log(request):
    form = LogMessageForm(request.POST or None)
    model = LogMessage
    LogMessages = LogMessage.objects.filter().order_by('-log_date').values
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.sent_by = request.user
            message.sent_from = request.user.username
            message.save()
            form = LogMessageForm
            return render(request, "parosmia/log.html", {"form": form,'message_list':LogMessages})

    else:
        form = LogMessageForm
        return render(request, "parosmia/log.html",{'form': form,'message_list':LogMessages})