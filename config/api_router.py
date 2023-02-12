from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from votos.users.api.views import UserViewSet
from votos.locations.api.views import MunicipalityViewSet, PollingStationViewSet, DepartmentViewSet, TableViewSet
from votos.voters.api.views import VoterViewSet, LeaderViewSet, AdministratorViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("voters", VoterViewSet)
router.register("leaders", LeaderViewSet)
router.register("administrators", AdministratorViewSet)
router.register("tables", TableViewSet)
router.register("polling-stations", PollingStationViewSet)
router.register("municipalities", MunicipalityViewSet)
router.register("departments", DepartmentViewSet)



app_name = "api"
urlpatterns = router.urls
