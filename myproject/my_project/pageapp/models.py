from django.db import models

# Create your models here.

class pagecontact(models.Model):
    name=models.CharField(max_length=123)
    email=models.EmailField(max_length=200)
    sub  =models.CharField(max_length=250, default=" ")
    cat  =models.CharField(max_length=238, default=" ")
    body=models.TextField(max_length=500)

    def __str__(self):
        return self.name


