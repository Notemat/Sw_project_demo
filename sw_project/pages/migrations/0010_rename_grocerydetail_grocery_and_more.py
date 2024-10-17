# Generated by Django 4.2.15 on 2024-10-14 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_rename_grocery_category_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GroceryDetail',
            new_name='Grocery',
        ),
        migrations.AlterModelOptions(
            name='groceryimage',
            options={'ordering': ['grocery'], 'verbose_name': 'Изображение к продукту', 'verbose_name_plural': 'Изображения к продукту'},
        ),
        migrations.RenameField(
            model_name='groceryimage',
            old_name='product',
            new_name='grocery',
        ),
    ]
