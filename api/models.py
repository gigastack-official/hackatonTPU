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

# Новые модели сенсоров

class LeakSensor(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"LeakSensor {self.value} at {self.timestamp}"

class LOSensor(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"LOSensor {self.value} at {self.timestamp}"

class ReedSwitch1(models.Model):
    is_triggered = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ReedSwitch1 {'Triggered' if self.is_triggered else 'Not Triggered'} at {self.timestamp}"

class ReedSwitch2(models.Model):
    is_triggered = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ReedSwitch2 {'Triggered' if self.is_triggered else 'Not Triggered'} at {self.timestamp}"

class DistanceSensor(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"DistanceSensor {self.value} at {self.timestamp}"

class CurrentSensor(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CurrentSensor {self.value} at {self.timestamp}"

class TemperatureSensor(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"TemperatureSensor {self.value} at {self.timestamp}"

class Gyroscope(models.Model):
    gyro_x = models.FloatField()
    gyro_y = models.FloatField()
    gyro_z = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Gyroscope ({self.gyro_x}, {self.gyro_y}, {self.gyro_z}) at {self.timestamp}"

class Accelerometer(models.Model):
    accel_x = models.FloatField()
    accel_y = models.FloatField()
    accel_z = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Accelerometer ({self.accel_x}, {self.accel_y}, {self.accel_z}) at {self.timestamp}"

class Fan(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fan {self.value} at {self.timestamp}"

# api/models.py

from django.db import models

class Command(models.Model):
    COMMAND_CHOICES = [
        ('pump', 'Помпа'),
        ('led', 'Лента'),
        ('servo1', 'Серво №1'),
        ('servo2', 'Серво №2'),
        ('auto_light', 'Авто-свет'),
        ('brightness', 'Яркость'),
        ('authorization', 'Авторизация'),
    ]

    command_type = models.CharField(max_length=20, choices=COMMAND_CHOICES)
    value = models.CharField(max_length=100)  # Можно использовать другой тип в зависимости от команды
    user_name = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_command_type_display()} - {self.value} at {self.timestamp}"
