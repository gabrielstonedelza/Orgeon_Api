# Generated by Django 4.0.1 on 2022-02-03 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgeon_api', '0004_delete_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partnership',
            name='partnership',
        ),
    ]
