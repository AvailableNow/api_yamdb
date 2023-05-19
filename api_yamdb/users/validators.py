import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


def validate_username(value):
    if value.lower() == 'me':
        raise ValidationError(
            gettext_lazy(f'{value} является служебным именем!')
        )
    if not re.match(r'[\w.@+-]+\Z', value):
        raise ValidationError(
            gettext_lazy(f'{value} содержит запрещённые символы')
        )
