# Generated by Django 2.2.13 on 2021-01-09 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20210109_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='public_profile',
        ),
    ]