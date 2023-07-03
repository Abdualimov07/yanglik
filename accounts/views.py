from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm, RegistrationForm, ProfileForm, UserEditForm, ProfileEditForm
from django.contrib.auth import logout
from .models import Profile, UserProfile

# Create your views here.

  
  
    
@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')

    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'pages/dashboard.html', {'form': form})
    



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(
                form.cleaned_data['password']
            )
            new_user.save()
            Profile.objects.create(user=new_user)
            # return redirect('login')
            context = { 
                'news_user': new_user 
            } 
            return render(request, 'account/register_done.html', context) 
    else:
        form = RegistrationForm()
    return render(request, 'account/registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')  
            else:
                form.add_error(None, 'Username yoki parolda xatolik bor')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('home_page')  

def edit_user(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()    
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/profile_edit.html', {'user_form': user_form, 'profile_form': profile_form})
            