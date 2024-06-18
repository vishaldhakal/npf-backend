# about/migrations/0016_cleanup_role_field.py
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0015_migrate_role_data"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ourteam",
            name="role",
        ),
        migrations.RenameField(
            model_name="ourteam",
            old_name="role_fk",
            new_name="role",
        ),
    ]
