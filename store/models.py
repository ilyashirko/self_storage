from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):
    email_adress = models.EmailField(default='Почта пользователя', verbose_name='Почта пользователя')

    def __str__(self):
        return self.email_adress


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='customer')
    photo = models.ImageField(verbose_name='Фото пользователя', null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True, max_length=10, verbose_name='Телефон пользователя')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Storage(models.Model):
    location_city = models.CharField(default='Москва', max_length=35, verbose_name='Город')
    location_street_name = models.CharField(default='Тверская', max_length=35, verbose_name='Улица')
    location_street_number = models.CharField(default='15', max_length=10, verbose_name='Идентификатор дома')
    store_temperature = models.DecimalField(verbose_name='Температура на складе', decimal_places=2, max_digits=5)
    ceiling_height = models.DecimalField(verbose_name='Высота потолка', decimal_places=2, max_digits=5)
    payment_per_month = models.IntegerField(verbose_name='Оплата за месяц')
    small_photo = models.ImageField(blank=True, verbose_name='Маленькое фото', default='image9.png')
    large_photo = models.ImageField(blank=True, verbose_name='Большое фото', default='image2.png')
    note = models.CharField(null=True, blank=True, max_length=35, verbose_name='Заметка')
    total_boxes = models.IntegerField(null=True)

    def __str__(self):
        return self.location_city


class Box(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент', blank=True, null=True, related_name='rented_boxes')
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, verbose_name='Склад', related_name='boxes')
    number = models.CharField(max_length=20, verbose_name='Номер в базе данных')
    in_use = models.BooleanField(default=False, verbose_name='Занятость бокса')
    rental_start_time = models.DateTimeField(null=True, verbose_name='Время начала аренды', blank=True)
    rental_end_time = models.DateTimeField(null=True, verbose_name='Время окончания аренды', blank=True)
    level = models.IntegerField(verbose_name='Этаж')
    square = models.IntegerField(verbose_name='Площадь', null=True)
    volume = models.IntegerField(verbose_name='Объём', null=True)
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return f'Бокс {self.number} склада {self.storage.location_city}'
