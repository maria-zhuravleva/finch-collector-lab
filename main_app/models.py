from django.db import models

class Finch(models.Model):
  name = models.CharField(max_length=100)
  species = models.CharField(max_length=100)
  color = models.CharField(max_length=50)
  wingspan = models.FloatField()
  lifespan = models.IntegerField()
  is_migratory = models.BooleanField(default=False)

  def __str__(self):
    return self.name
