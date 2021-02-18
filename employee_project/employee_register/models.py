from django.db import models



class Employee(models.Model):
    GENDER_CHOICES = (
        ('male', 'MALE'), 
        ('female', 'FEMALE'),
        ('transgender', 'TRANSGENDER'),
    )
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    age = models.CharField(max_length=5)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, default='male')
    address = models.CharField(max_length=100)
    eemail = models.EmailField()
    
    
