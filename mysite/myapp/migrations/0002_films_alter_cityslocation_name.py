# Generated by Django 4.1.6 on 2023-02-21 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.CharField(max_length=128)),
                ('descript', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='cityslocation',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Город'),
        ),
    ]
