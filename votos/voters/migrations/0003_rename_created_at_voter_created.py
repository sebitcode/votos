# Generated by Django 4.0.9 on 2023-02-11 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0002_administrator_leader_voter_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voter',
            old_name='created_at',
            new_name='created',
        ),
    ]
