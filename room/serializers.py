from rest_framework import serializers
from .models import Bed,Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class BedSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = Bed
        fields = '__all__'