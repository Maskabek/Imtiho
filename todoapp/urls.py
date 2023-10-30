from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('edit/<int:pk>', views.edit_todo, name='edit')
]
