from django.urls import path
from .views import MeasurementView, SensorView, MeasurementDetailView
urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', MeasurementDetailView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
