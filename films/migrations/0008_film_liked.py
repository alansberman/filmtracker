# Generated by Django 3.1.3 on 2020-11-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_auto_20201107_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='liked',
            field=models.BooleanField(null=True),
        ),
    ]
