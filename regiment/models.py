from django.db import models
from soliders.models import Soliders
from missions.models import Mission
# Create your models here.
class Regiment(models.Model):
    soliders = models.ManyToManyField(Soliders)
    regiment_id = models.AutoField(primary_key=True)
    missions_id = models.ManyToManyField(Mission)
