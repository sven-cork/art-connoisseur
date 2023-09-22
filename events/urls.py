from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.events, name='events'),
    path('submit_comment/', views.submit_comment, name='submit_comment'),
    path('load_comments/', views.load_comments, name='load_comments'),
    path('event_detail/<int:event_id>/', views.event_detail, name='event_detail'),  # Add this line
]
