from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import validate_username


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    USER_STATUSES = (
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (USER, 'Пользователь')
    )
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150,
        validators=[validate_username],
        unique=True,
    )
    bio = models.TextField(
        verbose_name='Коротко о себе',
        help_text='Биография',
        blank=True,
    )
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        unique=True,
        blank=False,
    )
    confirmation_code = models.CharField(
        verbose_name='Код подтверждения',
        max_length=200,
    )
    role = models.CharField(
        max_length=30,
        choices=USER_STATUSES,
        blank=False,
        default='user',
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    @property
    def is_admin(self):
        return self.role == User.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == User.MODERATOR or self.is_staff
