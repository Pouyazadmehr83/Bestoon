from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from json import JSONEncoder
from  .models import Expense,Income,Token,User
from datetime import datetime
# Create your views here.

@csrf_exempt
def submit_expense(request):
    # با .get() کار کن تا ارور نده
    this_token = request.POST.get('token')
    amount = request.POST.get('amount')
    description_text = request.POST.get('text')  # یا 'description'

    if not this_token or not amount or not description_text:
        return JsonResponse({"status": "error", "message": "missing fields"}, status=400)

    try:
        this_user = User.objects.get(token__token=this_token)
    except User.DoesNotExist:
        return JsonResponse({"status": "error", "message": "invalid token"}, status=401)

    try:
        amount = float(amount)  # یا Decimal، اما برای سادگی
    except ValueError:
        return JsonResponse({"status": "error", "message": "invalid amount"}, status=400)

    Expense.objects.create(
        user=this_user,
        amount=amount,
        description=description_text,  # ← اینجا description باشه، نه text
        # date رو نده، چون auto_now_add=True داره و خودش پر می‌کنه
    )

    return JsonResponse({"status": "success"})

@csrf_exempt
def submit_income(request):
    this_token = request.POST.get('token')
    amount = request.POST.get('amount')
    description_text = request.POST.get('text')  # یا 'description'

    if not this_token or not amount or not description_text:
        return JsonResponse({"status": "error", "message": "missing fields"}, status=400)

    try:
        this_user = User.objects.get(token__token=this_token)
    except User.DoesNotExist:
        return JsonResponse({"status": "error", "message": "invalid token"}, status=401)

    try:
        amount = float(amount)  # یا Decimal، اما برای سادگی
    except ValueError:
        return JsonResponse({"status": "error", "message": "invalid amount"}, status=400)

    Income.objects.create(
        user=this_user,
        amount=amount,
        description=description_text,  # ← اینجا description باشه، نه text
        # date رو نده، چون auto_now_add=True داره و خودش پر می‌کنه
    )

    return JsonResponse({"status": "success"})