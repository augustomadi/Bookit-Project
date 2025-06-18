from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReservaViewSet
from .views.availability import PropertyAvailabilityView

router = DefaultRouter()
router.register(r'reservations', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('properties/availability', PropertyAvailabilityView.as_view(), name='property-availability'),
] 