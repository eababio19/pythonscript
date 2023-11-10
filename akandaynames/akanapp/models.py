from django.db import models

class AkanName(models.Model):
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    akan_name = models.CharField(max_length=50)


    def __str__(self):
        return self.akan_name
