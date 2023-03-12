from django.urls import path

from .views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
]
# По гиту остается products и еще раз посмотреть url. Далее, заменить везде на static
# Попровить везде ссылки и В футере возле копирайта дописать текущий год через теги