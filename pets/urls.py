"""pet_house URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from .views import (
    PetDetailView,
    CatsListView,
    DogsListView,
    PetListView,
)

urlpatterns = [
    path('', PetListView.as_view(), name='pet-list'),
    path('<int:id>', PetDetailView.as_view(), name='pet-detail'),
    path('cats/', CatsListView.as_view(), name='cat-list'),
    path('dogs/', DogsListView.as_view(), name='dog-list')
]
