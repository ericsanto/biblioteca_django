# Generated by Django 5.0.2 on 2024-02-27 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_history_text_one_history_text_two'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='text_one',
        ),
        migrations.RemoveField(
            model_name='history',
            name='text_two',
        ),
    ]
