from django.db import IntegrityError
from django.contrib.auth.models import User

import environ
env = environ.Env(
    DEBUG=(bool, False)
)

try:
    superuser = User.objects.create_superuser(
        username=env('DJANGO_SUPERUSER_USERNAME', default="emran"),
        email=env('DJANGO_SUPERUSER_EMAIL', default="emran@gmail.com"),
        password=env('DJANGO_SUPERUSER_PASSWORD', default="1234"))
    superuser.save()
except IntegrityError:
    # print(f"Super User with username {env('DJANGO_SUPERUSER_USERNAME')} is already exit!")
    print("Super User with usernameis already exit!")
except Exception as e:
    print(e)
