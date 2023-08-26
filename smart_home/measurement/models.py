from django.db import models
from  django.utils import timezone

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor (models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=450)
class Measurement (models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name = 'measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add = True)
