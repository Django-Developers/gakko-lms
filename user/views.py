from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import ExtendedUserCreationForm, UserAuthenticationForm


def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')


@login_required
def profile(request):
    return render(request, 'example/profile.html')


def register(request):
    context = {}
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        # print('hello')
        if form.is_valid():
            print(form.save())

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('index')  # or home?
    else:  # GET request
        form = ExtendedUserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("index")
    if request.POST:
        form = UserAuthenticationForm(request.POST)
        # print(form)
        # if form.is_valid():
            # email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        print(username)
        print(password)
        if user:
            login(request, user)
            return redirect("index")
    else:
        form = UserAuthenticationForm()
    context['form'] = form
    return render(request, 'login.html', context)
