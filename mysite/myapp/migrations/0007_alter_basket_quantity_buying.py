# Generated by Django 4.1.5 on 2023-04-03 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_basket_quantity_buying'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='quantity_buying',
            field=models.IntegerField(verbose_name='Общее количество'),
        ),
    ]
