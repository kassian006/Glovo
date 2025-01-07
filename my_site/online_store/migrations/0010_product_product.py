# Generated by Django 5.1.4 on 2025-01-07 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0009_alter_product_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category_product', to='online_store.category'),
            preserve_default=False,
        ),
    ]
