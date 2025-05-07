from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Inscription réussie! Vous êtes maintenant connecté.")
            return redirect('home')
    else:
        form = RegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenue, {username}! Vous êtes maintenant connecté.")
                # Rediriger vers la page précédente si disponible
                next_page = request.GET.get('next')
                return redirect(next_page if next_page else 'home')
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('home')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')