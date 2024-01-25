from rest_framework import serializers
from .models import Bed,Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class BedSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(allow_null=True)

    class Meta:
        model = Bed
        fields = '__all__'
        
    def create(self, validated_data):
        patient_data = validated_data.pop('patient', None)
        bed_instance = Bed.objects.create(**validated_data)

        if patient_data:
            patient_instance = Patient.objects.create(**patient_data)
            bed_instance.patient = patient_instance
            bed_instance.save()

        return bed_instance
    
    def update(self, instance, validated_data):
        patient_data = validated_data.pop('patient', None)
        print(patient_data)

        instance = super(BedSerializer, self).update(instance, validated_data)
        
        if not instance.is_occupied and instance.patient:
            # instance.patient.delete() #uncomment if want to delete the patient after removing the patient from bed
            instance.patient = None
            instance.save()
            
        elif patient_data:
            patient_instance = instance.patient
            if patient_instance:
                for key, value in patient_data.items():
                    setattr(patient_instance, key, value)
                patient_instance.save()
            else:
                patient_instance = Patient.objects.create(**patient_data)
                instance.patient = patient_instance
                instance.save()

        return instance
    
    def assign_bed_to_existing_patient(self, bed_id, patient_id):
        try:
            bed_instance = Bed.objects.get(pk=bed_id)
            patient_instance = Patient.objects.get(pk=patient_id)

            bed_instance.patient = patient_instance
            bed_instance.is_occupied = True
            bed_instance.save()

            return bed_instance
        except Bed.DoesNotExist:
            raise serializers.ValidationError("Bed does not exist.")
        except Patient.DoesNotExist:
            raise serializers.ValidationError("Patient does not exist.")