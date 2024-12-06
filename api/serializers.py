from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    LightSensor, ColorSensor, WaterFlowSensor, MoistureSensor, OverflowSensor,
    LeakSensor, LOSensor, ReedSwitch1, ReedSwitch2, DistanceSensor,
    CurrentSensor, TemperatureSensor, Gyroscope, Accelerometer, Fan
)

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User(
            email=validated_data.get('email'),
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LightSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LightSensor
        fields = '__all__'

class ColorSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorSensor
        fields = '__all__'

class WaterFlowSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterFlowSensor
        fields = '__all__'

class MoistureSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoistureSensor
        fields = '__all__'

class OverflowSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverflowSensor
        fields = '__all__'

# Сериализаторы для новых моделей

class LeakSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeakSensor
        fields = '__all__'

class LOSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LOSensor
        fields = '__all__'

class ReedSwitch1Serializer(serializers.ModelSerializer):
    class Meta:
        model = ReedSwitch1
        fields = '__all__'

class ReedSwitch2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ReedSwitch2
        fields = '__all__'

class DistanceSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistanceSensor
        fields = '__all__'

class CurrentSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentSensor
        fields = '__all__'

class TemperatureSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureSensor
        fields = '__all__'

class GyroscopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gyroscope
        fields = '__all__'

class AccelerometerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accelerometer
        fields = '__all__'

class FanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fan
        fields = '__all__'


# api/serializers.py

from rest_framework import serializers
from .models import Command

class CommandSerializer(serializers.Serializer):
    pump = serializers.BooleanField(required=False)
    led = serializers.BooleanField(required=False)
    servo1 = serializers.BooleanField(required=False)
    servo2 = serializers.BooleanField(required=False)
    auto_light = serializers.BooleanField(required=False)
    brightness = serializers.FloatField(required=False)
    user_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    def validate_user_name(self, value):
        return value