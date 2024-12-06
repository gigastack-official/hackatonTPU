from django_filters import rest_framework as filters
from .models import (
    LightSensor, ColorSensor, WaterFlowSensor, MoistureSensor, OverflowSensor,
    LeakSensor, LOSensor, ReedSwitch1, ReedSwitch2, DistanceSensor,
    CurrentSensor, TemperatureSensor, Gyroscope, Accelerometer, Fan
)

class LightSensorFilter(filters.FilterSet):
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')
    start_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = LightSensor
        fields = ['min_value', 'max_value', 'start_date', 'end_date']

class ColorSensorFilter(filters.FilterSet):
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')
    is_detected = filters.BooleanFilter(field_name="is_detected")
    start_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = ColorSensor
        fields = ['min_value', 'max_value', 'is_detected', 'start_date', 'end_date']

class WaterFlowSensorFilter(filters.FilterSet):
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')
    start_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = WaterFlowSensor
        fields = ['min_value', 'max_value', 'start_date', 'end_date']

class MoistureSensorFilter(filters.FilterSet):
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')
    start_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = MoistureSensor
        fields = ['min_value', 'max_value', 'start_date', 'end_date']

class OverflowSensorFilter(filters.FilterSet):
    is_overflow = filters.BooleanFilter(field_name="is_overflow")
    start_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = OverflowSensor
        fields = ['is_overflow', 'start_date', 'end_date']

# Фильтры для новых моделей

class LeakSensorFilter(filters.FilterSet):
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')
    start_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = LeakSensor
        fields = ['min_value', 'max_value', 'start_date', 'end_date']

class LOSensorFilter(filters.FilterSet):
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')
    start_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = LOSensor
        fields = ['min_value', 'max_value', 'start_date', 'end_date']

class ReedSwitch1Filter(filters.FilterSet):
    is_triggered = filters.BooleanFilter(field_name="is_triggered")
    start_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = ReedSwitch1
        fields = ['is_triggered', 'start_date', 'end_date']

class ReedSwitch2Filter(filters.FilterSet):
    is_triggered = filters.BooleanFilter(field_name="is_triggered")
    start_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = ReedSwitch2
        fields = ['is_triggered', 'start_date', 'end_date']

class DistanceSensorFilter(filters.FilterSet):
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')
    start_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = DistanceSensor
        fields = ['min_value', 'max_value', 'start_date', 'end_date']

class CurrentSensorFilter(filters.FilterSet):
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')
    start_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = CurrentSensor
        fields = ['min_value', 'max_value', 'start_date', 'end_date']

class TemperatureSensorFilter(filters.FilterSet):
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')
    start_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = TemperatureSensor
        fields = ['min_value', 'max_value', 'start_date', 'end_date']

class GyroscopeFilter(filters.FilterSet):
    gyro_x_min = filters.NumberFilter(field_name="gyro_x", lookup_expr='gte')
    gyro_x_max = filters.NumberFilter(field_name="gyro_x", lookup_expr='lte')
    gyro_y_min = filters.NumberFilter(field_name="gyro_y", lookup_expr='gte')
    gyro_y_max = filters.NumberFilter(field_name="gyro_y", lookup_expr='lte')
    gyro_z_min = filters.NumberFilter(field_name="gyro_z", lookup_expr='gte')
    gyro_z_max = filters.NumberFilter(field_name="gyro_z", lookup_expr='lte')
    start_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = Gyroscope
        fields = ['gyro_x_min', 'gyro_x_max', 'gyro_y_min', 'gyro_y_max', 'gyro_z_min', 'gyro_z_max', 'start_date', 'end_date']

class AccelerometerFilter(filters.FilterSet):
    accel_x_min = filters.NumberFilter(field_name="accel_x", lookup_expr='gte')
    accel_x_max = filters.NumberFilter(field_name="accel_x", lookup_expr='lte')
    accel_y_min = filters.NumberFilter(field_name="accel_y", lookup_expr='gte')
    accel_y_max = filters.NumberFilter(field_name="accel_y", lookup_expr='lte')
    accel_z_min = filters.NumberFilter(field_name="accel_z", lookup_expr='gte')
    accel_z_max = filters.NumberFilter(field_name="accel_z", lookup_expr='lte')
    start_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = Accelerometer
        fields = ['accel_x_min', 'accel_x_max', 'accel_y_min', 'accel_y_max', 'accel_z_min', 'accel_z_max', 'start_date', 'end_date']

class FanFilter(filters.FilterSet):
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')
    start_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = Fan
        fields = ['min_value', 'max_value', 'start_date', 'end_date']
