# Generated by Django 4.1.7 on 2023-05-12 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CR', 'Curd'), ('ML', 'Milk'), ('LS', 'Lassi'), ('MS', 'Mlikshake'), ('PN', 'Paneer'), ('GH', 'Ghee'), ('CZ', 'Cheese'), ('IC', 'Ice-Creams')], max_length=2),
        ),
    ]
