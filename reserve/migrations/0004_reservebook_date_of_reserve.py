# Generated by Django 5.0.2 on 2024-02-26 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0003_remove_reservebook_number_of_reserve'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservebook',
            name='date_of_reserve',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data da reserva'),
        ),
    ]
