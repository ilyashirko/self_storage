# Generated by Django 4.1.2 on 2022-10-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_box_is_use'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='volume',
            field=models.CharField(max_length=10, null=True, verbose_name='Объём'),
        ),
    ]
