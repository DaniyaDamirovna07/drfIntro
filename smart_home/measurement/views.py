from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView,ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from rest_framework import viewsets
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer, MeasurementsSerializer



class SensorsAPIView(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    

class MeasurementList(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementsSerializer
    
# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
