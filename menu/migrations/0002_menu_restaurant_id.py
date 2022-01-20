# Generated by Django 4.0.1 on 2022-01-20 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_restaurant_large_cate_restaurant_small_cate'),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='restaurant_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant'),
            preserve_default=False,
        ),
    ]