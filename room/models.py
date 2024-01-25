from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    medication   = models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return self.name

class Bed(models.Model):
    is_occupied = models.BooleanField(default=False)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Bed {self.id} - {'Occupied' if self.is_occupied else 'Vacant'}"