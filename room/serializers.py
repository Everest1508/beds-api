from rest_framework import serializers
from .models import Beds

class BedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beds
        fields = ['bed_id','is_occuipied','patient_name','medication']