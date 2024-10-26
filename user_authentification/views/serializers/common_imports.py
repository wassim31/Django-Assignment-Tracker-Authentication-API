from rest_framework import serializers
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

User = get_user_model()

