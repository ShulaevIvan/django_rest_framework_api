# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView, ListAPIView
from .serializers import MeasurementDetailViewSerializer, SensorSerializer, SensorUpdateSerializer, MeasurementSerializer
from rest_framework.response import Response
from .models import Sensor, Measurement

class SensorView(CreateAPIView, ListAPIView):
    serializer_class = SensorSerializer

    def get_queryset(self):
        queryset = Sensor.objects.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save()
    

class UpdateSensorView(RetrieveUpdateAPIView):
    serializer_class = SensorUpdateSerializer

    def get_queryset(self):
        queryset = Sensor.objects.all()
        return queryset

    def perform_update(self, serializer):
        serializer.save()

    

class MeasurementView(CreateAPIView):
    
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    
    
class MeasurementDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = MeasurementDetailViewSerializer
    