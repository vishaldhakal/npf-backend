# Generated by Django 4.2.13 on 2024-06-18 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0018_role_hierarchy_level'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='role',
            options={'ordering': ['hierarchy_level']},
        ),
    ]
