# Generated by Django 4.2.13 on 2024-06-18 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0017_alter_ourteam_role_alter_role_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='hierarchy_level',
            field=models.IntegerField(default=100),
        ),
    ]
