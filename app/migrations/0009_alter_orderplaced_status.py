# Generated by Django 4.1.7 on 2023-06-27 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_payment_orderplaced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('On The Way', 'On The WAy '), ('Accepted', 'Accepted'), ('Cancel', 'Cancel'), ('Pending', 'Pending'), ('Packed', 'Packed')], default='pending', max_length=50),
        ),
    ]