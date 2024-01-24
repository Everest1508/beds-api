from django.db import models

# Create your models here.
class Beds(models.Model):
    bed_id       = models.AutoField(primary_key=True)
    is_occuipied = models.BooleanField(default=False)
    patient_name = models.CharField(max_length=200,blank=True,null=True)
    medication   = models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return str(self.bed_id)+" : "+('Occupied' if self.is_occuipied else 'Vacant')