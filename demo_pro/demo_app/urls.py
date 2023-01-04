from django.urls import path
from .import views


urlpatterns = [
    path('mess/',views.mess),
]