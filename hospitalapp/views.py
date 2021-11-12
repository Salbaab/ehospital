from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from userapp.views import farm_admin

# Create your views here.
def home(request):
    context ={}
    return render(request, 'hospital/index.html', context)

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("landingPage:login")
        messages.error(request, "Unsuccessful registration. Invalid information")
    form = NewUserForm()
    context ={"register_form":form}
    return render(request, 'hospital/register.html', context)

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("user_account:home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    context ={"login_form":form}
    template_name='hospital/login.html'
    return render(request, template_name, context )