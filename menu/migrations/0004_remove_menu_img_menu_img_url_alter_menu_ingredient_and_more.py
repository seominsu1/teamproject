# Generated by Django 4.0.1 on 2022-01-20 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_rename_restaurant_id_menu_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='img',
        ),
        migrations.AddField(
            model_name='menu',
            name='img_url',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='ingredient',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
