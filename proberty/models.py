from django.db import models
from django.contrib.gis.db import models
from django.utils import timezone


# Create your models here.

class Room (models.Model):
    name=models.CharField(max_length= 50)
    price=models.IntegerField()
    descripe=models.TextField(max_length=100)
    loc=models.PointField(srid =4326)
    a=models.Manager()
    image=models.ImageField(upload_to='proberty/', null=True)
    files=models.FileField( upload_to='proberty/', max_length=100,blank=True, null=True)
    category=models.ForeignKey('Category', related_name='room_category', on_delete=models.CASCADE)


 
    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'


class RoomImages (models.Model):
    room=models.ForeignKey(Room, related_name='room_image', on_delete=models.CASCADE)
    images=models.ImageField( upload_to='room_image/')

    def __str__(self):
        return str(self.room)



class Category (models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name


class RoomReview (models.Model):
    room=models.ForeignKey(Room, related_name='room_Review', on_delete=models.CASCADE)
    feedback=models.TextField(max_length=300)
    rate = models.IntegerField(default=0)
    def __str__(self):
        return str(self.room)

class RoomBook(models.Model):
    room=models.ForeignKey(Room, related_name='room_book', on_delete=models.CASCADE)
    name=models.CharField( max_length=100)
    email=models.EmailField( max_length=254)
    from_date=models.DateField(default=timezone.now)
    to_date=models.DateField(default=timezone.now)
    Guest=models.IntegerField(default=1)
    children=models.IntegerField(default=0)


    def __str__(self):
        return self.name







