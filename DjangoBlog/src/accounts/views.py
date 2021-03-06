from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
# Create your views here.
from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    title = "Login"
    next = request.GET.get("next")
    # print(request.user.is_authenticated())
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request,user)
        # print(request.user.is_authenticated())
        if next:
            return redirect(next)
        return redirect("/")
    return render(request,"form.html",{"form":form,"title":title})

def register_view(request):
    title = "register"
    next = request.GET.get("next")
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username,password=password)
        login(request,new_user)
        if next:
            return redirect(next)
        return redirect("/")
    context = {
        "form":form,
        "title":title,
    }
    return render(request,"form.html",context)

def logout_view(request):
    logout(request)
    return redirect("/")
    return render(request,"form.html",{})