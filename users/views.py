from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .forms import NewUserForm
from django.contrib import messages
from django.apps import apps
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect("users:login")
        #return HttpResponseRedirect(reverse("login"))
    Playlist=apps.get_model('playlist','Playlist')
    last_ten = Playlist.objects.filter(use=request.user.username).order_by('-id')[:10]
    return render(request, "users/user.html",{
        "playlistListed":last_ten
    })
    
def login_view(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        #print(username,password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("users:index")
        else:
            return render(request,"users/login.html",{
                "message":"Invalid credentials."
            })
    
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request,"users/login.html",{
        "message":"Logged Out."
    })
    

def register_request(request):
    if request.method=="POST":
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,"Registration successful.")
            return redirect("users:index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form= NewUserForm()
    return render(request=request,template_name="users/register.html",context={"register_form":form})
