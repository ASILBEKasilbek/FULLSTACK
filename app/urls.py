from .views import*
from django.urls import path



urlpatterns = [
    path('', main, name='main'),  
    path('register/', register_view, name='register'),  
    path('login/', login_view, name='login'),  
    path('logout/', logout_view, name='logout'), 
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('profile/',profile,name='profile'),
    path('services/',services,name='services'),
    path('home/', home, name='home'),  
    path('yordamlar/', yordamlar, name='yordamlar'),
]
