from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Gust,Movie,Reservation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GustSerializer,MovieSerializer,ReservationSerializer
from rest_framework import status,filters
# Create your views here.

@api_view(['GET','POST'])
def FBV_LIST(request):
    #GET
    if request.method == 'GET':
        guests = Gust.objects.all()
        serializer = GustSerializer(guests, many=True)
        return Response(serializer.data)
    
    #POST
    elif request.method == 'POST':
        serializer = GustSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        