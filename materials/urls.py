
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_materials, name='materials'),
    path('<int:material_id>/', views.material_detail, name='material_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:material_id>/', views.edit_product, name='edit_material'),
    path('delete/<int:material_id>/', views.delete_material, name='delete_material'),
]
