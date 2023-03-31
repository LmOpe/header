from django.urls import path
from . import views

urlpatterns = [
    path('api/whoami/', views.get_header, name="get_header"),
]