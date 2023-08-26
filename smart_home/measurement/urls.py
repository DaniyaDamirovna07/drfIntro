from django.urls import path, include
from measurement.views import  SensorsAPIView, MeasurementList
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'sensors', SensorsAPIView)
router.register(r'measurements', MeasurementList)

urlpatterns = [
    path('', include(router.urls)),

   
    # TODO: зарегистрируйте необходимые маршруты
]
