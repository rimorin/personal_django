from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='test endpoint'),
    path('updateUser/', views.update_user, name='update user record'),
    path('createUser/', views.set_user, name='create user record'),
    path('getUsers/', views.get_users, name='get all users record'),
    path('deleteUser/', views.delete_user, name='delete user record')
]