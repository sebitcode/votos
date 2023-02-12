from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "votos.locations"
    verbose_name = _("Locations")

    def ready(self):
        pass
