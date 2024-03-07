# Generated by Django 5.0.2 on 2024-03-06 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.book'),
        ),
    ]
