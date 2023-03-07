# Generated by Django 4.1.7 on 2023-03-07 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='имя продукта')),
                ('image', models.ImageField(blank=True, upload_to='product_images', verbose_name='изображение')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('short_desc', models.CharField(blank=True, max_length=100, verbose_name='краткое описание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='цена')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='количество на складе')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата обновления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productcategory', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]
