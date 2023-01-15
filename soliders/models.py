from django.db import models

# Create your models here.
class Soliders(models.Model):
    name = models.CharField(max_length=50)
    post =  models.CharField(max_length=100)
    sol_id = models.CharField(max_length=50)


    def __str__(self):
        return self.sol_id



class UserModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Leave_Letter_Form(models.Model):
    sol_id = models.ForeignKey(Soliders,on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    leave_from = models.DateField()
    leave_to = models.DateField()
    reason = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    date = models.DateField()
    is_approved =models.BooleanField(default=False)

    def __str__(self):
        return str(self.sol_id)