from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name or f'Категория с id - {self.pk}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='категория')
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='product_images', blank=True, verbose_name='изображение')
    description = models.TextField(verbose_name='описание', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание', max_length=100, blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='дата обновления', auto_now=True)

    def __str__(self):
        return self.name or f'Категория с id - {self.pk}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
