from django.urls import path
from . import views

app_name = "Super_Social"
urlpatterns = [
    path('', views.homepage, name='Home'),
    path('Super_Social/', views.SocialApp, name='app_page'),
    path('Person/<slug:slug>/', views.person, name='person'),
    path('products/', views.post_new, name='post_new'),

]