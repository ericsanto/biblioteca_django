# Generated by Django 5.0.2 on 2024-02-26 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservebook',
            name='date_of_devolution',
            field=models.DateField(blank=True, null=True, verbose_name='Data de devolução'),
        ),
        migrations.AlterField(
            model_name='reservebook',
            name='number_of_reserve',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Número da reserva'),
        ),
    ]