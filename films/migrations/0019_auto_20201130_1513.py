# Generated by Django 3.1.3 on 2020-11-30 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0018_auto_20201125_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
