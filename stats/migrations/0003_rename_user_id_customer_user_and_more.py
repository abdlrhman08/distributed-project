# Generated by Django 5.0.4 on 2024-04-27 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='stats',
            old_name='product_id',
            new_name='product',
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.customer'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='stats',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.stats'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stats',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stats',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='stats',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
