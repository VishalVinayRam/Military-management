from django.db import models
from missions.models import Mission

# Create your models here.
class Terrorist(models.Model):
    name = models.CharField(max_length=50)
    place =  models.CharField(max_length=50)
    id = models.AutoField(primary_key=True),
    Mission_captured = models.ForeignKey(Mission,on_delete=models.CASCADE)
    father_name = models.CharField(max_length=50)
    is_alive = models.BooleanField(default=True)

    def __str__(self):
        return self.name

