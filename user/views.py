from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,get_user_model
from .forms import ExtendedUserCreationForm

User = get_user_model()

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
            user_obj = form.save()
            print(user_obj)
            print(type(user_obj))
            # new_user = User.objects.create(username='')
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            print(username)
            print(password)
            user= authenticate(username=username, password=password)
            print(user)
            login(request, user_obj)
            return redirect('index')
    else:
        form = ExtendedUserCreationForm()   
            


    
    context={'form':form}
    return render(request,'user/register.html',context)
