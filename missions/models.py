from django.db import models
from ammon.models import Ammo
from soliders.models import Soliders



# Create your models here.

class Mission(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    date = models.DateField()
    lead = models.OneToOneField(Soliders,on_delete=models.CASCADE)
    ammo = models.ForeignKey(Ammo,on_delete=models.CASCADE)
    place = models.CharField(max_length=50)


    def __str__(self):
        return self.name