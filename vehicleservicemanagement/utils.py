import random
from django.core.mail import send_mail
from ..vehicle.models import OTP

def generate_otp(user):
    otp = ''.join(random.choices('0123456789', k=6))
    OTP.objects.update_or_create(user=user, defaults={'otp': otp})
    return otp

def send_otp_email(user):
    otp = generate_otp(user)
    send_mail(
        'Your OTP',
        f'Your OTP is: {otp}',
        'sender@example.com',
        [user.email],
        fail_silently=False,
    )

def verify_otp(user, otp):
    otp_obj = OTP.objects.filter(user=user, otp=otp).first()
    if otp_obj:
        # OTP is correct and valid, you can implement further actions here
        otp_obj.delete()
        return True
    else:
        # OTP is incorrect or expired
        return False