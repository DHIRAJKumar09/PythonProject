from django.db import models

# Create your models here.
from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    rank = models.IntegerField()

    def __str__(self):
        return self.name

