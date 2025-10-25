from django.urls import path
from .views import register_view
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_user, name='logout')
]
