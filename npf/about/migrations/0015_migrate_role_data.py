# about/migrations/0015_migrate_role_data.py
from django.db import migrations


def migrate_role_data(apps, schema_editor):
    OurTeam = apps.get_model("about", "OurTeam")
    Role = apps.get_model("about", "Role")

    for team_member in OurTeam.objects.all():
        role = Role.objects.get(name=team_member.role)
        team_member.role_fk = role
        team_member.save()


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0014_add_role_fk_to_ourteam"),
    ]

    operations = [
        migrations.RunPython(migrate_role_data),
    ]
