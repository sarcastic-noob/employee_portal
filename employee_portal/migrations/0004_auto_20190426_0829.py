# Generated by Django 2.2 on 2019-04-26 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_portal', '0003_auto_20190426_0827'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='status',
            new_name='leave_request_status',
        ),
    ]
