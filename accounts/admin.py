from django.contrib import admin
from .models import Profile, UserProfile

# Register your models here.
admin.site.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

admin.site.register(UserProfile,ProfileAdmin)   