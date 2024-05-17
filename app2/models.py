from django.db import models

# Create your models here.

class employee(models.Model):
    id=models.CharField(primary_key=True,max_length=200)
    name=models.CharField(max_length=50)
    salary=models.CharField(max_length=80)
    age=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
