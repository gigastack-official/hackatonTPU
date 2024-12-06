from django.contrib import admin
from .models import LightSensor, ColorSensor, WaterFlowSensor, MoistureSensor, OverflowSensor

@admin.register(LightSensor)
class LightSensorAdmin(admin.ModelAdmin):
    list_display = ('value', 'timestamp')
    list_filter = ('timestamp',)

@admin.register(ColorSensor)
class ColorSensorAdmin(admin.ModelAdmin):
    list_display = ('value', 'is_detected', 'timestamp')
    list_filter = ('is_detected', 'timestamp')

@admin.register(WaterFlowSensor)
class WaterFlowSensorAdmin(admin.ModelAdmin):
    list_display = ('value', 'timestamp')
    list_filter = ('timestamp',)

@admin.register(MoistureSensor)
class MoistureSensorAdmin(admin.ModelAdmin):
    list_display = ('value', 'timestamp')
    list_filter = ('timestamp',)

@admin.register(OverflowSensor)
class OverflowSensorAdmin(admin.ModelAdmin):
    list_display = ('is_overflow', 'timestamp')
    list_filter = ('is_overflow', 'timestamp')
