# Generated by Django 4.0.1 on 2022-01-27 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgeon_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userscheckedin',
            name='has_checked_in',
        ),
        migrations.AlterField(
            model_name='userscheckedin',
            name='check_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
