from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Beds
from .serializers import BedsSerializer
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def beds(request):
    if request.method == 'GET':
        beds = Beds.objects.all()
        serializer = BedsSerializer(beds, many=True)
        return Response({'Beds': serializer.data})
    
    if request.method == 'POST':
        bed = request.data
        if not bed['is_occuipied']:
            bed['patient_name'] = None
            bed['medication'] = None
        print(bed)
        serializer = BedsSerializer(data=bed)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE'])
def get_bed(request,id):
    
    try:
        bed = Beds.objects.get(pk=id)
    except Beds.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method=='GET':
        serializer = BedsSerializer(bed)
        return Response(serializer.data)
    if request.method == 'DELETE':
        bed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)