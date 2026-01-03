from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.mail import send_mail


@receiver(user_logged_in)
def send_login_email(sender, request, user, **kwargs):
    if not user.email:
        return

    send_mail(
        subject="ورود موفق به حساب کاربری",
        message=(
            f"سلام {user.username}\n\n"
            "ورود موفقی به حساب شما انجام شد.\n"
            "اگر این ورود توسط شما نبوده، لطفاً رمز عبور خود را تغییر دهید."
        ),
        from_email=None,
        recipient_list=[user.email],
        fail_silently=True,
    )
