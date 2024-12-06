from django.contrib import admin
from .models import Sensor, Device, Measurement, LightingMode

admin.site.register(Sensor)
admin.site.register(Device)
admin.site.register(Measurement)
admin.site.register(LightingMode)
