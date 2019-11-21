from django.urls import path
from apps.core import views

app_name='apps.core'

urlpatterns = [
    path('', views.home, name='home')
]
