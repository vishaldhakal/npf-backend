# Generated by Django 4.2.13 on 2024-06-16 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_event_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
