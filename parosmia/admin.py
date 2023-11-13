from django.contrib import admin
from .models import Person, LogMessage, Experience

admin.site.register(Person)
admin.site.register(LogMessage)
admin.site.register(Experience)
