from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.grupo4),
        url(r'^persona/', views.personas_list),
        
    ]
