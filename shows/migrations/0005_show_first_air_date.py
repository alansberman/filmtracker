# Generated by Django 3.1.3 on 2020-12-04 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0004_auto_20201204_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='first_air_date',
            field=models.DateField(null=True),
        ),
    ]