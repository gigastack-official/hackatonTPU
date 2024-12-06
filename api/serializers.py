from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Sensor, Device, Measurement, LightingMode

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

class SensorSerializer(serializers.ModelSerializer):
    """
       Сериализатор для модели Sensor, используемый для отображения и создания датчиков.
    """
    class Meta:
        model = Sensor
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class MeasurementSerializer(serializers.ModelSerializer):
    sensor_name = serializers.ReadOnlyField(source='sensor.name')
    class Meta:
        model = Measurement
        fields = '__all__'

class LightingModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LightingMode
        fields = '__all__'
