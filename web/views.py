from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponse
from .models import Expense, Income
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout as auth_logout,login as auth_login,login
from django.contrib import messages
from .forms import LoginForm
@login_required
def index(request):
    incomes = Income.objects.filter(user=request.user)  # تغییر نام متغیر
    expenses = Expense.objects.filter(user=request.user)  # تغییر نام متغیر
    context = {
        "incomes": incomes,  # مطابقت با template
        "expenses": expenses,  # مطابقت با template
    }
    return render(request, "web/dashboard.html", context)
@login_required
def profile(request):
    return render(request, "web/profile.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("psw")
        email = request.POST.get("email")

        if User.objects.filter(username=username).exists():
            messages.error(request, "❌ Username already exists")
            return redirect("web:register")
        
        User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        messages.success(request, "✅ Registration successful. Please log in.")
        return redirect("web:login")

    return render(request, "web/register.html")



def login_view(request):
    if request.user.is_authenticated:
        return redirect('web:index')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)  # ایجاد فرم از داده‌های POST
        if form.is_valid():  # اعتبارسنجی فرم
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'web:index')
                return redirect(next_url)
            else:
                messages.error(request, "❌ Invalid username or password")
    else:
        form = LoginForm()  # ایجاد فرم خالی برای GET request
    
    return render(request, 'web/login.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    messages.info(request, "👋 You logged out successfully")
    return redirect("web:login")



@login_required
@require_POST
def submit_expense(request):
    amount = request.POST.get("amount")
    description = request.POST.get("text")

    if not amount or not description:
        return JsonResponse({"error": "missing fields"}, status=400)

    Expense.objects.create(
        user=request.user,
        amount=amount,
        description=description
    )
    return JsonResponse({"status": "expense added"})



@login_required
@require_POST
def submit_income(request):
    amount = request.POST.get("amount")
    description = request.POST.get("text")

    if not amount or not description:
        return JsonResponse({"error": "missing fields"}, status=400)

    Income.objects.create(
        user=request.user,
        amount=amount,
        description=description
    )
    return JsonResponse({"status": "income added"})
