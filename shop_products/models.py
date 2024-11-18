from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """Класс категорий"""
    name = models.CharField(max_length=50, verbose_name='Наименование')
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='product/',
                              verbose_name='изображение', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Subcategory(models.Model):
    """Класс подкатегорий"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='категория')
    name = models.CharField(max_length=50, verbose_name='Наименование')
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='product/',
                              verbose_name='изображение', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'


class Product(models.Model):
    """Класс продуктов"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='категория')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE,
                                 verbose_name='подкатегория')
    name = models.CharField(max_length=50, verbose_name='Наименование')
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='product/',
                              verbose_name='изображение', **NULLABLE)
    price = models.IntegerField(verbose_name='цена')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'



