# Generated by Django 2.2 on 2019-04-26 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pay_slip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_and_year', models.CharField(max_length=25)),
                ('bonus', models.DecimalField(decimal_places=3, max_digits=5)),
                ('total', models.DecimalField(decimal_places=3, max_digits=10)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_portal.employees')),
                ('pay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_portal.cfti_matrix')),
            ],
            options={
                'unique_together': {('employee_id', 'month_and_year')},
            },
        ),
    ]
