from django.db import models

# Create your models here.

# Link https://www.geeksforgeeks.org/serializer-relations-django-rest-framework/

GENDER_CHOICES = (('M','Male'),('F','Female'),)
class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')
    age = models.CharField(max_length=3)
    nationId = models.CharField(max_length=8)
    county = models.CharField(max_length=30)
    
    class Meta:
        ordering=('nationId',)
        
    def __str__(self):
        return self.email

# The UserImmunization model holds a ManyToOne relationship with the User model
# The same immunization will not be assigned to more than one user, but one user can have multiple immunizations.
# Hence, the UserImmunizationSerializer class should serialize only a single user instance, whereas, UserSerializer class should serialize one or more userimuniserializer instances (more than one immunization can be assigned to an user). 
class UserImmunization(models.Model):
    immunizationName = models.CharField(max_length=30)
    immunizationDosageLevel=models.CharField(max_length=30)
    immunizationDate =models.CharField(max_length=20)
    nextImmunizationDate = models.CharField(max_length=30)
    user = models.ForeignKey(User,related_name='immunizations',on_delete=models.CASCADE) #NB: "user", "immunizations" must be the same as the one used in the serializers

class Meta:
    ordering = ('immunizationName',)
    def __str__(self):
        return self.immunizationName
