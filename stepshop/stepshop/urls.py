from django.contrib import admin
from django.urls import path, include

from stepshop.views import index, contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('products/', include('mainapp.urls', namespace='products')),
]
