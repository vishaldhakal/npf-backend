# Generated by Django 4.2.13 on 2024-06-18 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0016_cleanup_role_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourteam',
            name='role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='about.role'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]