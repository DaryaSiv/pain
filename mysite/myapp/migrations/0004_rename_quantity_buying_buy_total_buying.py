# Generated by Django 4.1.5 on 2023-03-29 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_basket_name_remove_basket_quantity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buy',
            old_name='quantity_buying',
            new_name='total_buying',
        ),
    ]