# Generated by Django 4.1.7 on 2023-02-27 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_cinemas_cinema_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Имя автора')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.FloatField(verbose_name='Цена')),
                ('quantity_buying', models.FloatField(verbose_name='Общая цена')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('genre', models.TextField()),
                ('year', models.SmallIntegerField(verbose_name='Год издания')),
                ('page', models.SmallIntegerField(verbose_name='Количество страниц')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('isbn', models.CharField(max_length=255, verbose_name='Исбн книги')),
                ('image', models.ImageField(upload_to='media')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.author')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.SmallIntegerField(verbose_name='Дата покупки')),
                ('total_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Банковская карта')),
            ],
            options={
                'verbose_name': 'Карта',
                'verbose_name_plural': 'Карты',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Язык')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
            },
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Способ оплаты')),
            ],
            options={
                'verbose_name': 'Способ оплаты',
                'verbose_name_plural': 'Способы оплаты',
            },
        ),
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Издательство')),
            ],
            options={
                'verbose_name': 'Издательство',
                'verbose_name_plural': 'Издательство',
            },
        ),
        migrations.RemoveField(
            model_name='cinema',
            name='city',
        ),
        migrations.DeleteModel(
            name='Films',
        ),
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.DeleteModel(
            name='Cinema',
        ),
        migrations.AddField(
            model_name='buy',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.card'),
        ),
        migrations.AddField(
            model_name='buy',
            name='pay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.pay'),
        ),
        migrations.AddField(
            model_name='buy',
            name='purchased_books',
            field=models.ManyToManyField(to='myapp.book'),
        ),
        migrations.AddField(
            model_name='buy',
            name='quantity_buying',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.basket'),
        ),
        migrations.AddField(
            model_name='buy',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customuser'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.language'),
        ),
        migrations.AddField(
            model_name='book',
            name='press',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.press'),
        ),
        migrations.AddField(
            model_name='basket',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.book'),
        ),
        migrations.AddField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customuser'),
        ),
    ]
