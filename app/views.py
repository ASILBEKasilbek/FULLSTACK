from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, SupportRequestForm
from .models import SupportRequest, FAQ

# Ro'yxatdan o'tish
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})

# Tizimga kirish
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'register/login.html', {'form': form})

# Tizimdan chiqish
def logout_view(request):
    logout(request)
    return redirect('login')

# Asosiy sahifa (home)
def main(request):
    return render(request, 'main.html')

# Contact sahifa
def contact(request):
    return render(request, 'contact.html')

# Yordamlar bo‘limi (FAQ)
def yordamlar(request):
    faqs = FAQ.objects.all()
    return render(request, 'yordamlar.html', {'faqs': faqs})

# Home sahifasida faqat hal qilingan muammolarni ko‘rsatish
def home_view(request):
    solved = SupportRequest.objects.filter(status='solved').order_by('-solved_at')[:10]
    return render(request, 'main.html', {'solved': solved})

# Xizmatlar (services) bo‘limi
@login_required
def services_view(request):
    form = SupportRequestForm()
    if request.method == 'POST':
        form = SupportRequestForm(request.POST)
        if form.is_valid():
            support = form.save(commit=False)
            support.user = request.user
            support.save()
            return redirect('services')

    user_requests = SupportRequest.objects.filter(user=request.user)
    solved = user_requests.filter(status='solved')
    pending = user_requests.filter(status='pending')

    return render(request, 'services.html', {
        'form': form,
        'solved': solved,
        'pending': pending,
    })

# Profil bo‘limi
@login_required
def profile_view(request):
    user_requests = SupportRequest.objects.filter(user=request.user)
    solved_requests = user_requests.filter(status='solved')
    pending_requests = user_requests.exclude(status='solved')
    return render(request, 'profile.html', {
        'solved_requests': solved_requests,
        'pending_requests': pending_requests,
    })
