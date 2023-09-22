from django.db import models

# Create your models here.
class Employee(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    city= models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.firstname}, {self.lastname}, {self.email}"