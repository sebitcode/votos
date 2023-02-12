from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_string_number(value):
    if not str(value).isnumeric():
        raise ValidationError(
            _('%(value)s is not a number'),
            params={'value': value},
        )
