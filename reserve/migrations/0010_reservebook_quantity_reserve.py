# Generated by Django 5.0.2 on 2024-03-12 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0009_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservebook',
            name='quantity_reserve',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Quantidade de agendamentos'),
        ),
    ]
