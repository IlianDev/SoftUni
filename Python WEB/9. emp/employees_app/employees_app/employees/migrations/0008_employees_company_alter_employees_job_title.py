# Generated by Django 4.0.2 on 2022-02-21 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_delete_testmodel_employees_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='company',
            field=models.CharField(choices=[('SoftUni', 'SoftUni'), ('Google', 'Google')], default='SoftUni', max_length=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employees',
            name='job_title',
            field=models.IntegerField(choices=[(1, 'Software Developer'), (2, 'QA_engineer'), (3, 'DevOps Specialist')]),
        ),
    ]
