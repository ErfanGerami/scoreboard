from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Score(models.Model):
    username=models.CharField(max_length=30)
    time=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1000)])
    maze_name=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.username}({self.maze_name}):{self.time}"
