# Generated by Django 3.1.3 on 2021-01-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0027_auto_20210106_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actingcredit',
            name='role',
            field=models.CharField(max_length=200, null=True),
        ),
    ]