from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

from api_yamdb.settings import USERNAME_NAME, EMAIL

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'

ROLE_CHOICES = (
    (USER, 'Пользователь'),
    (MODERATOR, 'Модератор'),
    (ADMIN, 'Администратор'),
)

MAX_LENGTH = max(len(choice[0]) for choice in ROLE_CHOICES)


def username_validator():
    """Функция для создания валидатора username."""

    return RegexValidator(
        regex=r'^[\w.@+-]+$',
        message='Username может содержать только буквы,'
                'цифры и символы @/./+/-/_.'
    )


class User(AbstractUser):
    """Пользователь"""
    username = models.CharField(
        max_length=USERNAME_NAME,
        unique=True,
        verbose_name='Имя пользователя',
        validators=[username_validator()]
    )

    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя',
        blank=True
    )

    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия',
        blank=True
    )

    role = models.CharField(
        max_length=MAX_LENGTH,
        choices=ROLE_CHOICES,
        default=USER,
        blank=True
    )
    email = models.EmailField(max_length=EMAIL, unique=True)
    bio = models.TextField(
        verbose_name='О себе',
        max_length=150,
        blank=True
    )
    confirmation_code = models.CharField(
        max_length=5,
        verbose_name='Код подтверждения',
        blank=True
    )

    @property
    def is_admin(self):
        return self.role == ADMIN or User.objects.filter(
            is_staff=True,
            is_superuser=True
        ).exists()

    @property
    def is_user(self):
        return self.role == USER

    @property
    def is_moderator(self):
        return self.role == MODERATOR
