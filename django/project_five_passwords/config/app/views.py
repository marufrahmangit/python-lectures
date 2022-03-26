from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'app/home.html')

@login_required
def special(request):
    return HttpResponse('You are logged in!')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            #hashing the password
            user.set_password(user.password)
            #save the hashed password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'app/registration.html',
                  {
                      'user_form':user_form,
                      'profile_form': profile_form,
                      'registered': registered,
                  })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('app:home'))
            else:
                return HttpResponse('Account not active')
        else:
            print('Someone tried to login and failed')
            print('Username: {} and password {}'.format(username,password))
            return HttpResponse('Invalid login details')
    else:
        return render(request,'app/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app:home'))