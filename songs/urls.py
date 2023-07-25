from django.urls import path
from .views import song_list, song_detail

urlpatterns = [
    path('api/music/', song_list, name='song-list'),
    path('api/music/<int:pk>/', song_detail, name='song-detail'),
]
