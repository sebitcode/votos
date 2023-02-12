from rest_framework import serializers

from votos.voters.models import Voter, Leader, Administrator

class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = ["id", "user_name", "names", "surnames", "address", "neighborhood", "cc", "leader", "table", "created"]
        extra_kwargs = {
            'user_name': {'read_only': True}
        }


class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = ["id", "user_name", "password", "names", "surnames", "address", "cc", "administrator"]
        extra_kwargs = {
            'user_name': {'read_only': True},
            'password': {'write_only': True}
        }

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ["id", "user_name", "password", "names", "surnames", "address", "cc"]
        extra_kwargs = {
            'user_name': {'read_only': True},
            'password': {'write_only': True}
        }
