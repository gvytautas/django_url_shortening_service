from django.urls import path
from .views import index, resolve, benchmark

urlpatterns = [
    path('', index, name='index'),
    path('benchmark', benchmark, name='benchmark'),
    path('<slug:short_url>', resolve, name='resolve_1'),
    path('<slug:short_url>/', resolve, name='resolve_2'),
]