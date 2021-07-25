from django.urls import path
from .views import Index, Room

urlpatterns = [
	path('', Index.as_view(), name='index'),
	path('<str:room_name>/', Room.as_view(), name='room'),
]