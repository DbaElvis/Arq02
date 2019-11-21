from django.urls import path, include
from apps.funcionarios import views
from .views import FuncionariosList
from .views import home



urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', FuncionariosList.as_view(), name='list_funcionarios'),
]

from django.urls import path



