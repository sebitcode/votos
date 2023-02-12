from django.db.models import CharField, Model, ForeignKey, BigIntegerField, CASCADE
from django.utils.translation import gettext_lazy as _

from .validators import validate_positive

class Table(Model):
    """
    Default custom user model for Votos.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # Required Info
    number = BigIntegerField(_("Number"), validators=[validate_positive])
    votes = BigIntegerField(_("Votes"), validators=[validate_positive], default=0)

    # Relations
    polling_station = ForeignKey("locations.PollingStation", verbose_name=_("PollingStation"), on_delete=CASCADE, related_name="tables")

    class Meta:
        unique_together = ('number', 'polling_station',)

class PollingStation(Model):
    """
    Default custom user model for Votos.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # Required Info
    name = CharField(_("Name"), max_length=255)
    address = CharField(_("Address"), max_length=255)

    # Relations
    municipality = ForeignKey("locations.Municipality", verbose_name=_("Municipality"), on_delete=CASCADE, related_name="polling_stations")

    class Meta:
        unique_together = ('name', 'municipality',)

class Municipality(Model):
    """
    Default custom user model for Votos.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # Required Info
    name = CharField(_("Name"), max_length=255)

    # Relations
    department = ForeignKey("locations.Department", verbose_name=_("Department"), on_delete=CASCADE, related_name="municipalities")

    class Meta:
        unique_together = ('name', 'department',)

class Department(Model):
    """
    Default custom user model for Votos.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # Required Info
    name = CharField(_("Name"), max_length=255, unique=True)
