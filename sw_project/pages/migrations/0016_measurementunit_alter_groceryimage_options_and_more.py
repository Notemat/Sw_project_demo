# Generated by Django 4.2.15 on 2024-11-20 07:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_alter_grocery_options_groceryimage_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasurementUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Полное название единицы измерения')),
                ('abbreviation', models.CharField(max_length=5, verbose_name='Сокращение единицы измерения')),
            ],
            options={
                'verbose_name': 'Единица измерения',
                'verbose_name_plural': 'Единицы измерения',
                'ordering': ['abbreviation'],
            },
        ),
        migrations.AlterModelOptions(
            name='groceryimage',
            options={'ordering': ['grocery'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.CreateModel(
            name='GroceryValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(verbose_name='Объём тары продукта')),
                ('grocery_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volumes', to='pages.groceryimage', verbose_name='Продукт')),
                ('measurement_unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pages.measurementunit', verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Объём тары продукта',
                'verbose_name_plural': 'Объём тары продуктов',
                'ordering': ['grocery_image'],
            },
        ),
    ]
