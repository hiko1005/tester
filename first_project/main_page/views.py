from django.shortcuts import render, redirect, HttpResponsePermanentRedirect
from .UserService import UserService
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, template_name="index.html")

def signup(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method =="GET":
        return render(request, template_name="signup.html")
    user = UserService.create(request.POST['login'], request.POST['password'])
    if str(request.POST['login']).strip == "" or str(request.POST['password']).strip == "":
        context = {"error": "user not created"}
        return render(request, 'signup.html', context)
    if user:
        login(request, user)
        return redirect("index")
    else:
        context = {"error": "user not created"}
        return render(request, 'signup.html', context)

def signin(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "GET":
        return render(request, "signin.html")
    
    user = authenticate(username=request.POST['login'], password=request.POST['password'])
    context = {}
    if user:
        login(request, user)
        return redirect("index")
    else:
        context['error'] = 'not authorized'
        return render(request, "signin.html", context)
    
def signout(request):
    logout(request)
    return HttpResponsePermanentRedirect("/index")
