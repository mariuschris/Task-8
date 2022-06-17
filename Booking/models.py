from django.db import models


# Create your models here.

    

class Lodging(models.Model):
    full_name = models.CharField(max_length=1500)
    email = models.EmailField(max_length=1500)
    occupation = models.CharField(max_length=1500)
    room_number = models.PositiveIntegerField(unique=True)
    amount_paid = models.IntegerField()
    number_of_night  = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.full_name
