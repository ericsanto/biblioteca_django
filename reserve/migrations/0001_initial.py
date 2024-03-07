# Generated by Django 5.0.2 on 2024-02-26 12:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0002_author_alter_category_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReserveBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_devolution', models.DateField(verbose_name='Data de devolução')),
                ('number_of_reserve', models.CharField(max_length=10, verbose_name='Número da reserva')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='library.book', verbose_name='Livro')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]
