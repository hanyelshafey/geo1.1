from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Room (models.Model):
    name=models.CharField(max_length= 50)
    price=models.IntegerField()
    descripe=models.TextField(max_length=100)
    loc=models.PointField(srid =4326)

    def __str__(self):
        return self.name

    class Meta:

        managed = True
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'