# Generated by Django 5.0.2 on 2024-03-08 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image_detail',
            field=models.ImageField(blank=True, null=True, upload_to='img_detail_books/'),
        ),
    ]
