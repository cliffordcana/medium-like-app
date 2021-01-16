# Generated by Django 2.2.13 on 2021-01-11 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0051_remove_customuser_access_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]