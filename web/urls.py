from django.urls import path

from .views import *

app_name = "web"

urlpatterns = [
    path("submit/expense/", submit_expense, name="submit_expense") ,
    path("submit/income/", submit_income, name="submit_income")   
]