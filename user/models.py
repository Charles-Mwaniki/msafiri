from django.db import models

# Create your models here.

class User(models.Model):
    userId=models.IntegerField()
    register_date = models.DateField(auto_now=True)
    firstName = models.CharField( max_length=20 )
    lastName = models.CharField( max_length=20 )
    IDnumber = models.IntegerField()
    contact = models.IntegerField()
    email = models.EmailField( max_length=50 )
    DateOfBirth = models.DateField()
    address = models.CharField( max_length=50 )
    code = models.IntegerField()
    town = models.CharField( max_length=30 )
    accountPin = models.IntegerField()
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField( max_length=20, choices=gender_choices, )
    married_choices = (
        ('S', 'single'),
        ('M', 'married'),
    )
    marital = models.CharField( max_length=10, choices=married_choices )
    employed = models.BooleanField()
    image = models.ImageField()

    def __str__(self):
        return self.firstName
