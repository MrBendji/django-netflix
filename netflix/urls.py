from django.urls import path
from .views import index_view, register_view, login_view, logout_view, watch_movie_view

urlpatterns = [
    path('', index_view, name='home'),
    path('login', login_view, name='login'),
    path('register', register_view, name='register'),
    path('logout', logout_view, name='logout'),
    path('watch', watch_movie_view, name='watch_movie'),
    path('index', index_view, name='home'),
]