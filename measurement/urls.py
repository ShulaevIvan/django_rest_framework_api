from django.urls import path
from .views import MeasurementView, SensorView, MeasurementDetailView, UpdateSensorView
urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', MeasurementDetailView.as_view()),
    path('sensors/<pk>/', UpdateSensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
