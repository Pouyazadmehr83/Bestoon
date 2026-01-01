from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse,HttpResponse
from json import JSONEncoder
from  .models import Expense,Income,User
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

#register
@csrf_exempt
@require_POST
def register_api(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")

    if not username or not password:
        return JsonResponse({"error": "missing fields"}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "user exists"}, status=400)

    User.objects.create_user(
        username=username,
        password=password,
        email=email
    )

    return JsonResponse({"status": "registered"})

#login@require_POST
@csrf_exempt
@require_POST
def login_api(request):
    user = authenticate(
        request,
        username=request.POST.get("username"),
        password=request.POST.get("password")
    )

    if not user:
        return JsonResponse({"error": "invalid credentials"}, status=401)

    login(request, user)  # ⭐ sessionid ساخته می‌شود
    return JsonResponse({"status": "logged in"})
@csrf_exempt
def logout_api(request):
    logout(request)
    return JsonResponse({"status": "logged out"})

@csrf_exempt
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

@csrf_exempt
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
