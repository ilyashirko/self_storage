# Generated by Django 4.1.2 on 2022-10-06 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_box_rental_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.customer', verbose_name='Клиент'),
        ),
    ]
