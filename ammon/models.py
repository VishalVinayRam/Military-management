
from django.db import models


# Create your models here.
class Ammo(models.Model):
    id = models.AutoField(primary_key=True)
    day_of_purchase = models.DateField()
    # missionid = models.ForeignKey(Mission, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    checkup = models.BooleanField(default=False)


    
    def __str__(self):
        return self.name

