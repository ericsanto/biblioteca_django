# Generated by Django 5.0.2 on 2024-02-26 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_author_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='imagens_livros/', verbose_name='Imagem'),
        ),
    ]