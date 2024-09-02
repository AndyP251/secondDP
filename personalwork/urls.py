from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('pull_canvas/', views.pull_canvas_data, name='pull_canvas'),
    path('add_schedule/', views.add_schedule, name='add_schedule'),
    path('update_event_layer/', views.update_event_layer, name='update_event_layer'),
    path('delete_event/', views.delete_event, name='delete_event'),
]