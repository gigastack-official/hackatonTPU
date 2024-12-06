from django.contrib import admin
from .models import (
    LightSensor, ColorSensor, WaterFlowSensor, MoistureSensor, OverflowSensor,
    LeakSensor, LOSensor, ReedSwitch1, ReedSwitch2, DistanceSensor,
    CurrentSensor, TemperatureSensor, Gyroscope, Accelerometer, Fan
)

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

# Регистрация новых моделей

@admin.register(LeakSensor)
class LeakSensorAdmin(admin.ModelAdmin):
    list_display = ('value', 'timestamp')
    list_filter = ('timestamp',)

@admin.register(LOSensor)
class LOSensorAdmin(admin.ModelAdmin):
    list_display = ('value', 'timestamp')
    list_filter = ('timestamp',)

@admin.register(ReedSwitch1)
class ReedSwitch1Admin(admin.ModelAdmin):
    list_display = ('is_triggered', 'timestamp')
    list_filter = ('is_triggered', 'timestamp')

@admin.register(ReedSwitch2)
class ReedSwitch2Admin(admin.ModelAdmin):
    list_display = ('is_triggered', 'timestamp')
    list_filter = ('is_triggered', 'timestamp')

@admin.register(DistanceSensor)
class DistanceSensorAdmin(admin.ModelAdmin):
    list_display = ('value', 'timestamp')
    list_filter = ('timestamp',)

@admin.register(CurrentSensor)
class CurrentSensorAdmin(admin.ModelAdmin):
    list_display = ('value', 'timestamp')
    list_filter = ('timestamp',)

@admin.register(TemperatureSensor)
class TemperatureSensorAdmin(admin.ModelAdmin):
    list_display = ('value', 'timestamp')
    list_filter = ('timestamp',)

@admin.register(Gyroscope)
class GyroscopeAdmin(admin.ModelAdmin):
    list_display = ('gyro_x', 'gyro_y', 'gyro_z', 'timestamp')
    list_filter = ('timestamp',)

@admin.register(Accelerometer)
class AccelerometerAdmin(admin.ModelAdmin):
    list_display = ('accel_x', 'accel_y', 'accel_z', 'timestamp')
    list_filter = ('timestamp',)

@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    list_display = ('value', 'timestamp')
    list_filter = ('timestamp',)
