from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, viewsets

from votos.voters.models import Voter, Leader, Administrator
from votos.locations.models import Table

from .serializers import VoterSerializer, LeaderSerializer, AdministratorSerializer

from .permissions import BlockLeaderPermission, BlockLeaderAutoCreatePermission


class VoterViewSet(RetrieveModelMixin, CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = VoterSerializer
    queryset = Voter.objects.all()
    lookup_field = "user_name"

    def get_queryset(self):
        user = self.request.user
        data = self.request.GET.dict()
        q_data = {}
        if data.get("leader_id", "").isnumeric():
            q_data["leader_id"] = data.get("leader_id")
        if data.get("table_id", "").isnumeric():
            q_data["table_id"] = data.get("table_id")
        if data.get("municipio_id", "").isnumeric():
            q_data["mesa__polling_station__municipality__id"] = data.get("municipio_id")
        if user.username.split("_")[-1] == "leader":
            return super().get_queryset().filter(leader=Leader.objects.filter(user_name=self.request.user.username).first(), **q_data)
        return super().get_queryset().filter(**q_data)

    def create(self, request, *args, **kwargs):
        request.data["leader"] = Leader.objects.filter(user_name=request.user.username).first()
        if request.data["leader"]:
            request.data["leader"] = request.data["leader"].pk
        response = super().create(request, *args, **kwargs)
        table = Table.objects.filter(pk=request.data["table"]).first()
        table.votes += 1
        table.save(update_fields=["votes"])
        return response

    @action(detail=False, methods=['get'])
    def count(self, request, pk=None):
        data = self.request.GET.dict()
        q_data = {}
        if data.get("leader_id", "").isnumeric():
            q_data["leader_id"] = data.get("leader_id")
        if data.get("table_id", "").isnumeric():
            q_data["table_id"] = data.get("table_id")
        if data.get("municipio_id", "").isnumeric():
            q_data["mesa__polling_station__municipality__id"] = data.get("municipio_id")
        return Response({'total': super().get_queryset().filter(**q_data).count()})

class LeaderViewSet(RetrieveModelMixin, CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = LeaderSerializer
    permission_classes = [IsAuthenticated, BlockLeaderAutoCreatePermission]
    queryset = Leader.objects.all()
    lookup_field = "user_name"

    def get_queryset(self):
        user = self.request.user
        if user.username.split("_")[-1] == "administrator":
            return Leader.objects.filter(administrator=Administrator.objects.filter(user_name=self.request.user.username).first())
        if user.username.split("_")[-1] == "leader":
            return Leader.objects.filter(user_name=self.request.user.username)
        return super().get_queryset()

    def get_object(self):
        user = self.request.user
        if user.username.split("_")[-1] == "leader":
            return Leader.objects.filter(user_name=self.request.user.username).first()
        return super().get_object()

    def create(self, request, *args, **kwargs):
        request.data["administrator"] = Administrator.objects.filter(user_name=request.user.username).first()
        if request.data["administrator"]:
            request.data["administrator"] = request.data["administrator"].pk
        return super().create(request, *args, **kwargs)

class AdministratorViewSet(RetrieveModelMixin, CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = AdministratorSerializer
    permission_classes = [IsAuthenticated, BlockLeaderPermission]
    queryset = Administrator.objects.all()
    lookup_field = "user_name"

    def get_queryset(self):
        user = self.request.user
        if user.username.split("_")[-1] == "administrator":
            return Administrator.objects.filter(user_name=self.request.user.username)
        return super().get_queryset()

    def get_object(self):
        user = self.request.user
        if user.username.split("_")[-1] == "administrator":
            return Administrator.objects.filter(user_name=self.request.user.username).first()
        return super().get_object()
