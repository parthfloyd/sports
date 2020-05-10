from django.db import models

# Create your models here.
class Match(models.Model):
	location = models.CharField(max_length = 64)
	sport = models.CharField(max_length = 64)
	maxPlayers = models.IntegerField()
	timeDate = models.DateTimeField()