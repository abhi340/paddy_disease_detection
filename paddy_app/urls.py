from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('upload/', views.upload_image, name='upload_image'),
    path('results/', views.results, name='results'),
    path('search/', views.search_users, name='search_users'),
    path('send-request/<int:to_user_id>/', views.send_request, name='send_request'),
    path('requests/', views.view_requests, name='view_requests'),
    path('authorize-users/', views.authorize_users, name='authorize_users'),
]
