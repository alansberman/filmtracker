# Generated by Django 3.1.3 on 2020-11-25 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0015_filmcredit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmcredit',
            name='credit_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
