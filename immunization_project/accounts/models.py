from django.db import models

# Create your models here.

class MyUser(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    
    

    def __str__(self):
        return self.firstName+' '+self.lastName
