from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_ROLE = (
        ('inspector', 'Инспектор'),
        ('office', 'Офис'),
        ('client', 'Клиент'),
    )
    phone = models.CharField('Телефон', max_length=50, blank=True)
    role = models.CharField('Роль пользователя', null=True, blank=True, choices=USER_ROLE, max_length=50)
