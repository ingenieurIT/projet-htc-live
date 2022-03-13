from django.contrib import admin

# Register your models here.

from .models import Admin, Imagesordi, Message, Ordinateur, Categorie, Like

admin.site.register(
    [Admin, Ordinateur, Message, Categorie, Like,
    Imagesordi])