# Generated by Django 4.0.2 on 2022-02-21 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_alter_employees_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='egn',
            field=models.CharField(default='', max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
