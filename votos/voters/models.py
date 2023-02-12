from django.db.models import CharField, Model, ForeignKey, DateTimeField, SET_NULL, CASCADE
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import (
    check_password,
    make_password,
)
from .validators import validate_string_number
from slugify import slugify

from django.contrib.auth import get_user_model

User = get_user_model()


class Voter(Model):
    """
    Default custom user model for Votos.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # Required Info
    names = CharField(_("Names"), max_length=255)
    surnames = CharField(_("Surnames"), max_length=255)
    user_name = CharField(
        verbose_name=_("User name"),
        max_length=100,
        null=True,
        blank=True
    )
    cc = CharField(_("Citizenship card"), max_length=255, validators=[validate_string_number])
    address = CharField(_("Address"), max_length=255)

    # Extra Info
    neighborhood = CharField(_("Neighborhood"), blank=True, max_length=255)
    created = DateTimeField(auto_now_add=True, blank=True)

    # Relations
    leader = ForeignKey("voters.Leader", verbose_name=_("Leader"), on_delete=SET_NULL, null=True, related_name="voters")
    table = ForeignKey("locations.Table", verbose_name=_("Table"), on_delete=CASCADE, related_name="voters")

    class Meta:
        unique_together = ('cc', 'user_name',)

    def save(self, *args, **kwargs):
        self.user_name = slugify(" ".join([word for word in f"{self.names} {self.surnames}".split(" ") if word not in ["", " "]]), separator="_")
        return super().save(*args, **kwargs)

class Leader(Model):
    """
    Default custom user model for Votos.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # Required Info
    names = CharField(_("Names"), max_length=255)
    surnames = CharField(_("Surnames"), max_length=255)
    user_name = CharField(
        verbose_name=_("User name"),
        max_length=100,
        null=True,
        blank=True
    )
    password = CharField(_("password"), max_length=128)
    address = CharField(_("Address"), max_length=255)
    cc = CharField(_("Citizenship card"), max_length=255, validators=[validate_string_number])

    # Relations
    administrator = ForeignKey("voters.Administrator", verbose_name=_("Administrator"), on_delete=SET_NULL, null=True, related_name="leaders")

    _password = None

    class Meta:
        unique_together = ('cc', 'user_name',)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """

        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)

    def save(self, *args, **kwargs):
        user = User.objects.filter(username=self.user_name).first()
        self.user_name = slugify(" ".join([word for word in f"{self.names} {self.surnames} Leader".split(" ") if word not in ["", " "]]), separator="_")
        if user:
            user.username = self.user_name
            user.password = self.password
            user.save(update_fields=["username", "password"])
        else:
            self.set_password(self.password)
            User.objects.create(username=self.user_name, password=self.password)
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        user = User.objects.filter(username=self.user_name).first()
        if user:
            user.delete()
        return super().delete(*args, **kwargs)

class Administrator(Model):
    """
    Default custom user model for Votos.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # Main Info
    names = CharField(_("Names"), max_length=255)
    surnames = CharField(_("Surnames"), max_length=255)
    user_name = CharField(
        verbose_name=_("User name"),
        max_length=100,
        null=True,
        blank=True
    )
    password = CharField(_("password"), max_length=128)
    address = CharField(_("Address"), max_length=255)
    cc = CharField(_("Citizenship card"), max_length=255, validators=[validate_string_number])

    _password = None

    class Meta:
        unique_together = ('cc', 'user_name',)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """

        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)

    def save(self, *args, **kwargs):
        user = User.objects.filter(username=self.user_name).first()
        self.user_name = slugify(" ".join([word for word in f"{self.names} {self.surnames} Administrator".split(" ") if word not in ["", " "]]), separator="_")
        if user and (user.username != self.user_name or  self.password != user.password):
            user.username = self.user_name
            user.password = self.password
            user.save(update_fields=["username", "password"])
        else:
            self.set_password(self.password)
            User.objects.create(username=self.user_name, password=self.password)
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        user = User.objects.filter(username=self.user_name).first()
        if user:
            user.delete()
        return super().delete(*args, **kwargs)
