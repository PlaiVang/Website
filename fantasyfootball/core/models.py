from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as necessary

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # Add more fields as necessary
