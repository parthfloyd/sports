from django.db import models
from django.contrib.auth.models import User

# Extending user model to store more data
class UserProfile (models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE, null= True)
	matches = models.ManyToManyField('Match',blank =True, related_name = "players")
	age = models.IntegerField(null=True)
	city = models.CharField(max_length = 200, null = True)

	def __str__(self):
		return self.user.username

# Match Model to store all the data related to Matches.
class Match(models.Model):
	location = models.CharField(max_length = 64)
	sport = models.CharField(max_length = 64)
	maxPlayers = models.IntegerField()
	date = models.DateField()
	time = models.TimeField()

	def __str__(self):
		return "ID : " + str(self.id) + " " + self.sport
