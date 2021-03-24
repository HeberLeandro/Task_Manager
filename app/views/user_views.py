from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def signup_user(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('task_list')
    else:
        user_form = UserCreationForm()
    return render(request, 'users/user_form.html', {'user_form': user_form})


def signin_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            messages.error(request, "User credentials are incorrect.")
            return redirect('signin')
    else:
        singin_form = AuthenticationForm()
    return render(request, 'users/singin.html', {"singin_form": singin_form})


def signout_user(request):
    logout(request)
    return redirect('signin')
