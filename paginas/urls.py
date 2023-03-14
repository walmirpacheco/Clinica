from django.urls import path

from .views import PaginaInicial

urlpatterns = [    
    path('index/', PaginaInicial.as_view(), name='index'),    
]