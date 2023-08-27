
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_materials, name='materials'),
    path('<material_id>', views.material_detail, name='material_detail'),
]
