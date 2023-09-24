from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/', views.follow_us, name='follow_us'),   
]
