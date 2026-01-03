import requests
from django.conf import settings

def verify_recaptcha(token):
    response = requests.post(
        "https://www.google.com/recaptcha/api/siteverify",
        data={
            "secret": settings.RECAPTCHA_SECRET_KEY,
            "response": token
        }
    )
    result = response.json()
    print("reCAPTCHA result:", result)
    return result.get("success") and result.get("score", 0) > 0.5
