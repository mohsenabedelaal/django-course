from django.db import models

# Create your models here.
# class Cards:
#     title : str
#     text : str
#     img : str
#     offer : bool

class Cards(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)