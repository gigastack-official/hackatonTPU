from rest_framework import serializers
from django.contrib.auth.models import User


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

from rest_framework import serializers
from .models import LightSensor, ColorSensor, WaterFlowSensor, MoistureSensor, OverflowSensor

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
