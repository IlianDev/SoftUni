# Generated by Django 4.0.2 on 2022-02-16 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0020_department'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
    ]
