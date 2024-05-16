from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    rollno=models.IntegerField()
    def __str__(self):
        return self.name
    

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    def __str__(self):
        return self.firstname
    
    



    
