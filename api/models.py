from django.db import models

class LightSensor(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"LightSensor {self.value} at {self.timestamp}"

class ColorSensor(models.Model):
    value = models.FloatField()
    is_detected = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ColorSensor {self.value} - {'Detected' if self.is_detected else 'Not Detected'} at {self.timestamp}"

class WaterFlowSensor(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"WaterFlowSensor {self.value} at {self.timestamp}"

class MoistureSensor(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"MoistureSensor {self.value} at {self.timestamp}"

class OverflowSensor(models.Model):
    is_overflow = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OverflowSensor {'Overflow' if self.is_overflow else 'Normal'} at {self.timestamp}"
