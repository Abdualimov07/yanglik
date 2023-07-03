from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)



class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('parol')    
        confirm_password = cleaned_data.get('parolni takrorlash')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Parol mos kelmadi")

    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        return user
    
    


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']        

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['date_of_birth', 'photo'] 