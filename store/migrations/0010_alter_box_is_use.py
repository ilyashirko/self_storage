# Generated by Django 4.1.2 on 2022-10-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_box_volume_alter_box_square'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='is_use',
            field=models.BooleanField(default=False, verbose_name='Занятость бокса'),
        ),
    ]
