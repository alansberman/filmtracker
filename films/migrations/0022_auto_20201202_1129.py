# Generated by Django 3.1.3 on 2020-12-02 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0021_auto_20201202_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommendation',
            old_name='name',
            new_name='title',
        ),
    ]
