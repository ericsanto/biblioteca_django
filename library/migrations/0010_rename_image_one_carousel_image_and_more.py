# Generated by Django 5.0.2 on 2024-02-28 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_carousel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carousel',
            old_name='image_one',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='image_three',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='image_two',
        ),
    ]
