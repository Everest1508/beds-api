from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Patient, Bed
from .serializers import PatientSerializer, BedSerializer

class PatientListCreateView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientDetailView(APIView):
    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BedListCreateView(APIView):
    def get(self, request):
        beds = Bed.objects.all()
        serializer = BedSerializer(beds, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BedDetailView(APIView):
    def get(self, request, pk):
        bed = get_object_or_404(Bed, pk=pk)
        serializer = BedSerializer(bed)
        return Response(serializer.data)

    def put(self, request, pk):
        bed = get_object_or_404(Bed, pk=pk)
        serializer = BedSerializer(bed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bed = get_object_or_404(Bed, pk=pk)
        bed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AssignBedToPatientView(APIView):
    def put(self, request, pk, *args, **kwargs):
        bed_id = pk
        patient_id = request.data.get('patient', {}).get('id')

        try:
            bed_instance = Bed.objects.get(pk=bed_id)
            patient_instance = Patient.objects.get(pk=patient_id)

            # Manually update the bed instance
            bed_instance.patient = patient_instance
            bed_instance.is_occupied = True
            bed_instance.save()

            serializer = BedSerializer(bed_instance)
            return Response(serializer.data)
        except Bed.DoesNotExist:
            return Response({"error": "Bed does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Patient.DoesNotExist:
            return Response({"error": "Patient does not exist."}, status=status.HTTP_404_NOT_FOUND)