# Generated by Django 4.0.2 on 2022-02-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_employees_company_alter_employees_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='company',
            field=models.CharField(choices=[('SoftUni', 'SoftUni'), ('Google', 'Google'), ('Facebook', 'Facebook')], max_length=8),
        ),
    ]
