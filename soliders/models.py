from django.db import models

# Create your models here.
class Soliders(models.Model):
    name = models.CharField(max_length=50)
    post =  models.CharField(max_length=100)
    sol_id = models.AutoField(primary_key=True),



class UserModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name