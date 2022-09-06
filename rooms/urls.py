from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_all_rooms),
    path("<int:room_id>", views.view_room),
]
