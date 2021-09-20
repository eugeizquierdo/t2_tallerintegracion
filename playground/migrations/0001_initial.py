# Generated by Django 3.2.7 on 2021-09-17 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('league', models.URLField()),
                ('players', models.URLField()),
                ('self', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Jugadores',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('position', models.CharField(max_length=50)),
                ('times_trained', models.IntegerField()),
                ('league', models.URLField()),
                ('team', models.URLField()),
                ('self', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Ligas',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('sport', models.CharField(max_length=50)),
                ('teams', models.URLField()),
                ('players', models.URLField()),
                ('self', models.URLField()),
            ],
        ),
    ]