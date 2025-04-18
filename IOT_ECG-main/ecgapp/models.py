# your_app/models.py
from django.db import models

class BloodPressure(models.Model):
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class HealthData(models.Model):
    temperature = models.FloatField()
    bpm = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
