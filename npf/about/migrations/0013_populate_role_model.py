# about/migrations/0013_populate_role_model.py
from django.db import migrations


def populate_roles(apps, schema_editor):
    OurTeam = apps.get_model("about", "OurTeam")
    Role = apps.get_model("about", "Role")

    existing_roles = OurTeam.objects.values_list("role", flat=True).distinct()

    for role_name in existing_roles:
        if role_name:
            Role.objects.create(name=role_name)


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0012_create_role_model"),
    ]

    operations = [
        migrations.RunPython(populate_roles),
    ]
