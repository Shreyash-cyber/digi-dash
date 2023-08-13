from django.urls import path
from .views import *
from . import views

app_name = 'users'

urlpatterns = [
    path('home/',views.home,name='home'), 
    path('', views.my_login, name='login'),   
    path('logout/',views.user_logout,name='logout'), 
    path('api-data/', chart_data.as_view(), name='api_data') 
    
]