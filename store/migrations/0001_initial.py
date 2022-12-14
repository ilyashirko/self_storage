# Generated by Django 4.1.2 on 2022-10-05 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_adress', models.EmailField(default='Почта пользователя', max_length=254, verbose_name='Почта пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Новый пользователь', max_length=35, verbose_name='Имя пользователя')),
                ('last_name', models.CharField(blank=True, max_length=35, null=True, verbose_name='Фамилия пользователя')),
                ('email_adress', models.EmailField(default='Почта пользователя', max_length=254, verbose_name='Почта пользователя')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото пользователя')),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Телефон пользователя')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_city', models.CharField(default='Москва', max_length=35, verbose_name='Город')),
                ('location_street_name', models.CharField(default='Тверская', max_length=35, verbose_name='Улица')),
                ('location_street_number', models.CharField(default='15', max_length=10, verbose_name='Идентификатор дома')),
                ('store_temperature', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Температура на складе')),
                ('ceiling_height', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Высота потолка')),
                ('payment_per_month', models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Оплата за месяц')),
                ('photo', models.IntegerField(blank=True, verbose_name='Фото')),
                ('note', models.CharField(blank=True, max_length=35, null=True, verbose_name='Заметка')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, verbose_name='Номер в базе данных')),
                ('is_use', models.BooleanField(default=False, verbose_name='Занятость склада')),
                ('rental_start_time', models.DateTimeField(null=True, verbose_name='Время начала аренды')),
                ('rental_end_time', models.DateTimeField(null=True, verbose_name='Время окончания аренды')),
                ('level', models.IntegerField(verbose_name='Этаж')),
                ('square', models.IntegerField(verbose_name='Площадь')),
                ('price', models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Цена')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer', verbose_name='Клиент')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.storage', verbose_name='Склад')),
            ],
        ),
    ]
