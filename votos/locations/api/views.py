from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from votos.locations.models import Municipality, PollingStation, Department, Table

from .serializers import MunicipalitySerializer, PollingStationSerializer, DepartmentSerializer, TableSerializer

from .permissions import BlockLeaderPermission

class TableViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin, GenericViewSet):
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated, BlockLeaderPermission]
    queryset = Table.objects.all()
    lookup_field = "id"

class PollingStationViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin, GenericViewSet):
    serializer_class = PollingStationSerializer
    permission_classes = [IsAuthenticated, BlockLeaderPermission]
    queryset = PollingStation.objects.all()
    lookup_field = "id"

class MunicipalityViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin, GenericViewSet):
    serializer_class = MunicipalitySerializer
    permission_classes = [IsAuthenticated, BlockLeaderPermission]
    queryset = Municipality.objects.all()
    lookup_field = "id"

class DepartmentViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin, GenericViewSet):
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, BlockLeaderPermission]
    queryset = Department.objects.all()
    lookup_field = "id"
