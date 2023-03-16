from django.urls import path

from authapp.views import logout, login

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    ]
