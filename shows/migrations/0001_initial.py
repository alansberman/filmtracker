# Generated by Django 3.1.3 on 2020-11-09 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('original_language', models.CharField(max_length=200)),
                ('original_name', models.CharField(max_length=200)),
                ('type_of_show', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('overview', models.TextField(null=True)),
                ('movie_db_id', models.IntegerField(null=True)),
                ('comments', models.CharField(max_length=200, null=True)),
                ('popularity', models.FloatField(null=True)),
                ('number_of_seasons', models.IntegerField(null=True)),
                ('number_of_episodes', models.IntegerField(null=True)),
                ('genres', models.CharField(max_length=200, null=True)),
                ('runtime', models.IntegerField(null=True)),
                ('vote_average', models.FloatField(null=True)),
                ('added', models.BooleanField(null=True)),
                ('wishlisted', models.BooleanField(null=True)),
                ('score', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('season_number', models.IntegerField()),
                ('overview', models.CharField(max_length=200, null=True)),
                ('movie_db_id', models.IntegerField()),
                ('number_of_episodes', models.IntegerField()),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.show')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('season_number', models.IntegerField()),
                ('overview', models.CharField(max_length=200, null=True)),
                ('movie_db_id', models.IntegerField()),
                ('episode_number', models.IntegerField()),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.season')),
            ],
        ),
    ]
