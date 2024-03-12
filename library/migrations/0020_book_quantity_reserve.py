# Generated by Django 5.0.2 on 2024-03-12 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0019_alter_author_description_alter_book_pdf_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity_reserve',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Quantidade de reservas'),
        ),
    ]