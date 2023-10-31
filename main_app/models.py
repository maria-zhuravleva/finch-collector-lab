from django.db import models
from django.urls import reverse

class Finch(models.Model):
  name = models.CharField(max_length=100)
  species = models.CharField(max_length=100)
  color = models.CharField(max_length=50)
  wingspan = models.FloatField()
  lifespan = models.IntegerField()
  is_migratory = models.BooleanField(default=False)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('finch-detail', kwargs={'finch_id': self.id})
