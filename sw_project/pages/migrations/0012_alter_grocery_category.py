# Generated by Django 4.2.15 on 2024-10-15 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_alter_grocery_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='grocery_category', to='pages.category', verbose_name='Категория продукта'),
        ),
    ]
