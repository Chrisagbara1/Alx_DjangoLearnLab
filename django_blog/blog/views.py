from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import RegisterForm, ProfileForm


class BlogLoginView(LoginView):
    template_name = "blog/login.html"
    redirect_authenticated_user = True


class BlogLogoutView(LogoutView):
    template_name = "blog/logout.html"


def register(request):
    """User registration using extended UserCreationForm with email."""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            messages.success(request, "Welcome! Your account was created.")
            return redirect("blog:profile")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})


@login_required
def profile(request):
    """Simple profile page to view/update first/last name + email."""
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("blog:profile")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "blog/profile.html", {"form": form})
