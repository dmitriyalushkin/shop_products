# Generated by Django 5.1.3 on 2024-11-18 18:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='изображение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_products.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'подкатегория',
                'verbose_name_plural': 'подкатегории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='изображение')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_products.category', verbose_name='категория')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_products.subcategory', verbose_name='подкатегория')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]
