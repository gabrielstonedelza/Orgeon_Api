# Generated by Django 4.0.1 on 2022-02-25 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgeon_api', '0016_remove_report_time_posted_alter_report_date_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportcomments',
            name='time_created',
        ),
    ]