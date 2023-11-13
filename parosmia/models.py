from django.db import models
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags import humanize

from django.utils import timezone
from django.conf import settings

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete =models.SET_NULL, null = True)
    log_date = models.DateTimeField("Experience Date")
    type = models.CharField(max_length=10) # Food, Medication, Mood, Symptoms, Exercise, Smells 
    quantity = models.CharField(max_length=40,blank=True, null=True)
    description = models.CharField(max_length=100,blank=True, null=True)
    rating = models.IntegerField()
    smells_like = models.CharField(max_length=100,blank=True, null=True)  

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.user}' added {self.type} experience"

    def colour(self):
        match(self.type):
            case 'mood': return "#ffff00"
            case 'smell': return "#00ff00"
            case 'medication': return "#ff00ff"
            case 'food': return "#ff0000"
            case 'symptom': return "#00ffff"
            case _: return  "#eeeedd"


class Person(models.Model):
    username  = models.CharField(max_length = 70)
    first_name = models.CharField(max_length = 70)
    last_name = models.CharField(max_length = 70)
    email = models.CharField(max_length = 100)
    password =  models.CharField(max_length = 70)
    
    def __str__(self):
        return self.first_name

class LogMessage(models.Model):
    
    sent_by = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    sent_from = models.CharField(max_length=100)
    message = models.CharField(max_length=1500)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' sent by {self.sent_by}"
    
    def get_date(self):
        return humanize.naturaltime(self.log_date)

