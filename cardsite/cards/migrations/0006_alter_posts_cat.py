# Generated by Django 5.1.5 on 2025-02-06 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_category_posts_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cards.category'),
        ),
    ]
