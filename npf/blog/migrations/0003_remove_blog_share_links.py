# Generated by Django 4.2.13 on 2024-06-03 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_social_links_alter_blog_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='share_links',
        ),
    ]
