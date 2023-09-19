from django.contrib import admin

# Register your models here.
# admin.py

from .models import ContactFormEntry

admin.site.register(ContactFormEntry)
