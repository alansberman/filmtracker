# Generated by Django 3.1.3 on 2020-11-18 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_person_known_for'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='movie_db_id',
            field=models.IntegerField(null=True),
        ),
    ]