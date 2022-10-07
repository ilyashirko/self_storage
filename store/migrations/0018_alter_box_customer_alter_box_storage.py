# Generated by Django 4.1.2 on 2022-10-07 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_box_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.customer', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='box',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boxes', to='store.storage', verbose_name='Склад'),
        ),
    ]
