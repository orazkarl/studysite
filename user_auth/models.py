from django.db import models
from django.contrib.auth.models import AbstractUser

from mainapp.models import Template1
class User(AbstractUser):
    USER_ROLE = (
        ('inspector', 'Инспектор'),
        ('office', 'Офис'),
        ('client', 'Клиент'),
    )
    phone = models.CharField('Телефон', max_length=50, blank=True)
    role = models.CharField('Роль пользователя', null=True, blank=True, choices=USER_ROLE, max_length=50)
    client_templates1 = models.ManyToManyField(Template1, verbose_name='Шаблоны', related_name='client')