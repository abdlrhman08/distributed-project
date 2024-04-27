# Generated by Django 5.0.4 on 2024-04-27 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0003_rename_user_id_customer_user_and_more'),
        ('store', '0003_alter_product_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='store.product'),
        ),
    ]
