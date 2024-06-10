from django.db import models

# Create your models here.

class Menu(models.Model):
    # id: int
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'pics')
    price = models.IntegerField()
    des = models.TextField()
    offer = models.BooleanField(default = False)