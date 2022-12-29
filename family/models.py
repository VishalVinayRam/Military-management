from django.db import models
from soliders.models import Soliders
# Create your models here.
class Family(models.Model):
    # solider_id =  models.ForeignKey(Soliders,on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    number = models.IntegerField()