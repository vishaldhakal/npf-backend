# Generated by Django 4.2.13 on 2024-06-19 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_opportunitytype_opportunity'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunitytype',
            name='slug',
            field=models.SlugField(blank=True, max_length=1000, null=True, unique=True),
        ),
    ]
