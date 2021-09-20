from django.db import models

# Create your models here.

class Ligas(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    sport = models.CharField(max_length=50)
    teams = models.URLField(max_length = 200)
    players = models.URLField(max_length = 200)
    self = models.URLField(max_length = 200)

class Equipos(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    league = models.URLField(max_length = 200)
    players = models.URLField(max_length = 200)
    self = models.URLField(max_length = 200)

class Jugadores(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    position = models.CharField(max_length=50)
    times_trained = models.IntegerField()
    league = models.URLField(max_length = 200)
    team = models.URLField(max_length = 200)
    self = models.URLField(max_length = 200)

# Cada liga debe tener los siguientes atributos:
# ● ID. (string)
# ● Name. (string)
# ● Sport. (string)
# ● Teams. (url)
# 4
# ● Players. (url)
# 5
# ● Self. (url)
# 6
# Cada equipo debe tener los siguientes atributos:
# ● ID. (string)
# ● Name. (string)
# ● City. (string)
# ● League. (url)
# ● Players. (url)
# ● Self. (url)
# Finalmente, cada jugador debe tener los siguientes atributos:
# ● ID. (string)
# ● Name. (string)
# ● Age. (int)
# ● Position. (string)
# ● Times Trained. (int)
# ● League. (url)
# ● Team. (url)
# ● Self. (url)

