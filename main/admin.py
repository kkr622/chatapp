from django.contrib import admin

# Register your models here.

from .models import Talk, User

admin.site.register(User)
admin.site.register(Talk)