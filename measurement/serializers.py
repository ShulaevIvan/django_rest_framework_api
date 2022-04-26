from rest_framework import serializers
from .models import Sensor, Measurement

class SensorSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Sensor
        fields = ['id', 'name', 'description', 'image']
        
class SensorUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Sensor
        fields = ['id', 'description']
        
class MeasurementSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        sensor = SensorSerializer(read_only=False)
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']
        
class MeasurementDetailViewSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)
    class Meta:
        
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements', 'image']

