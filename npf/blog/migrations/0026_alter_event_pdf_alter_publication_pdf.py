# Generated by Django 4.2.13 on 2024-08-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_blog_views_count_event_views_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
    ]