# Generated by Django 3.1.3 on 2020-11-05 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='added_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Date Added'),
        ),
    ]