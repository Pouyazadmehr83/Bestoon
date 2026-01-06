from django.urls import path
from .views import *

app_name = "web"

urlpatterns = [
    path("", index, name="index"),
    path("submit/expense/", submit_expense, name="submit_expense"),
    path("submit/income/", submit_income, name="submit_income"),

    path("account/profile/", profile, name="profile"),
    path("account/register/", register, name="register"),
    path("account/login/", login_view, name="login"),
    path("account/logout/", logout_view, name="logout"),
]
