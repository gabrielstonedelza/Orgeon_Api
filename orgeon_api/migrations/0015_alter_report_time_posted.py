# Generated by Django 4.0.1 on 2022-02-25 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgeon_api', '0014_alter_report_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='time_posted',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
