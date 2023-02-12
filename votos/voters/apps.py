from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "votos.voters"
    verbose_name = _("Voters")

    def ready(self):
        pass
