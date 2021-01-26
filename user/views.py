from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authentication, login
from .forms import ExtendedUserCreationForm

def index(request):
    if request.user.is_authenticated:
        username=request.user.username
    else:
        username='not logged in'
    context={'username' : username}
    return render(request, 'user/index.html', context)
@login_required
def profile(request):
    return render(request, 'example/profile.html')
def register(request):
    if request.method=="POST":
        form=ExtendedUserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user= authentication(username=username, password=password)
            login(request, user)

            return redirect('index')
    else:
        from = ExtendedUserCreationForm()       


    
    context={'form':form}
    return render(request,'user/register.html')
