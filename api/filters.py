from django_filters import rest_framework as filters
from .models import LightSensor, ColorSensor, WaterFlowSensor, MoistureSensor, OverflowSensor

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
