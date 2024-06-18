# about/migrations/0012_create_role_model.py
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0011_alter_donation_image_alter_image_src_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
