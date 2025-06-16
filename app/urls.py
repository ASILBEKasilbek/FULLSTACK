from .views import*
from django.urls import path
from . import views

urlpatterns = [
    path('register/', register_view, name='register'),  
    path('login/', login_view, name='login'),  
    path('logout/', logout_view, name='logout'), 
    path('contact/',contact,name='contact'),
    path('yordamlar/', yordamlar, name='yordamlar'),
    path('', views.home_view, name='main'),
    path('services/', views.services_view, name='services'),
    path('profile/', views.profile_view, name='profile'),
]
