from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/update/<int:pk>/', views.post_update, name='post_update'),
    path('post/delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

