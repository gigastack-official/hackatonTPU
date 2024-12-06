from django.db import models
from django.contrib.auth.models import User

# Пример модели датчика
class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # Параметры датчика (приведены в качестве примера)
    color = models.CharField(max_length=50, blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)  # объем жидкости
    fluid_level = models.FloatField(blank=True, null=True)  # уровень жидкости
    leakage = models.BooleanField(default=False)  # датчик протечки
    fill_level = models.FloatField(blank=True, null=True)  # уровень наполнения
    illumination = models.FloatField(blank=True, null=True)  # освещенность
    voc = models.FloatField(blank=True, null=True)  # летучие органические соединения
    co2 = models.FloatField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    energy_consumption = models.FloatField(blank=True, null=True)  # энергопотребление
    gyro_data = models.CharField(max_length=100, blank=True, null=True)  # данные гироскопа
    accelerometer_data = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

# Пример модели исполнительного устройства
class Device(models.Model):
    DEVICE_TYPE_CHOICES = [
        ('pump', 'Pump'),
        ('fan', 'Fan'),
        ('servo', 'Servo (door/window)'),
        ('led', 'LED Strip'),
    ]

    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=20, choices=DEVICE_TYPE_CHOICES)
    is_active = models.BooleanField(default=False)  # состояние включен/выключен
    # Дополнительные параметры, например яркость для LED
    brightness = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

# Модель для хранения истории измерений
class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    timestamp = models.DateTimeField(auto_now_add=True)
    # Данные измерения (может быть JSON или отдельные поля)
    fluid_level = models.FloatField(blank=True, null=True)
    co2 = models.FloatField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    illumination = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"Measurement for {self.sensor.name} at {self.timestamp}"

# Модель режима освещения
class LightingMode(models.Model):
    mode_name = models.CharField(max_length=100, unique=True)
    # Например, «auto» - умное освещение, «manual» - ручное, и т.д.
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.mode_name
