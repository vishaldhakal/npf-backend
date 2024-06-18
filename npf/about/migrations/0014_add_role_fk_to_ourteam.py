# about/migrations/0014_add_role_fk_to_ourteam.py
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0013_populate_role_model"),
    ]

    operations = [
        migrations.AddField(
            model_name="ourteam",
            name="role_fk",
            field=models.ForeignKey(
                null=True, on_delete=models.SET_NULL, to="about.Role"
            ),
        ),
    ]
