from django.urls import path

from .views import *

app_name = "web"

urlpatterns = [
    path("  ", submit_expense, name="submit_expense") ,
    path("submit/income/", submit_income, name="submit_income"),
    path("account/register/", register_api, name="register_api"),
    path("account/login/", login_api, name="login_api"),
    path("account/logout/", logout_api, name="logout_api"),

]