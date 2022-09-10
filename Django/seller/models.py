from django.db import models

# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=50)
    password = models.CharField(max_length=20,null=True,blank=True)
    pic = models.FileField(upload_to='seller profile',default='avtar.png')

    def __str__(self):
        return self.name