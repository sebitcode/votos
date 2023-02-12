from django.core.management.base import BaseCommand, CommandError

from votos.voters.models import Voter, Leader, Administrator
from votos.locations.models import Table, PollingStation, Municipality, Department

from django.contrib.auth import get_user_model

User = get_user_model()

import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        f_departments = open('votos/locations/management/commands/utils/departments.json')
        f_municipalities = open('votos/locations/management/commands/utils/municipalities.json')
        f_polling_stations = open('votos/locations/management/commands/utils/polling-stations.json')
        f_tables = open('votos/locations/management/commands/utils/tables.json')
        f_administrators = open('votos/locations/management/commands/utils/administrators.json')
        f_leaders = open('votos/locations/management/commands/utils/leaders.json')
        f_voters = open('votos/locations/management/commands/utils/voters.json')

        departments = json.load(f_departments)
        municipalities = json.load(f_municipalities)
        polling_stations = json.load(f_polling_stations)
        tables = json.load(f_tables)
        administrators = json.load(f_administrators)
        leaders = json.load(f_leaders)
        voters = json.load(f_voters)

        User.objects.all().delete()

        Department.objects.all().delete()
        for department in departments:
            Department.objects.create(**department)

        f_departments.close()

        Municipality.objects.all().delete()
        for municipality in municipalities:
            department = Department.objects.get(name=municipality["department"])
            municipality["department"] = department
            Municipality.objects.create(**municipality)

        f_municipalities.close()

        PollingStation.objects.all().delete()
        for polling_station in polling_stations:
            municipality = Municipality.objects.get(name=polling_station["municipality"])
            polling_station["municipality"] = municipality
            PollingStation.objects.create(**polling_station)

        f_polling_stations.close()

        Table.objects.all().delete()
        for table in tables:
            polling_station = PollingStation.objects.get(name=table["polling_station"])
            table["polling_station"] = polling_station
            Table.objects.create(**table)

        f_tables.close()

        Administrator.objects.all().delete()
        for administrator in administrators:
            Administrator.objects.create(**administrator)

        f_administrators.close()

        Leader.objects.all().delete()
        for leader in leaders:
            administrator = Administrator.objects.get(user_name=leader["administrator"])
            leader["administrator"] = administrator
            Leader.objects.create(**leader)

        f_leaders.close()

        Voter.objects.all().delete()
        for voter in voters:
            leader = Leader.objects.get(user_name=voter["leader"])
            voter["leader"] = leader
            table = Table.objects.get(number=voter["table"])
            voter["table"] = table
            Voter.objects.create(**voter)

        f_voters.close()
