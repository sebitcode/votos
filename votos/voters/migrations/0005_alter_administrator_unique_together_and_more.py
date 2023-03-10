# Generated by Django 4.0.9 on 2023-02-12 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0004_alter_administrator_cc_alter_leader_cc_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='administrator',
            unique_together={('cc', 'user_name')},
        ),
        migrations.AlterUniqueTogether(
            name='leader',
            unique_together={('cc', 'user_name')},
        ),
        migrations.AlterUniqueTogether(
            name='voter',
            unique_together={('cc', 'user_name')},
        ),
    ]
