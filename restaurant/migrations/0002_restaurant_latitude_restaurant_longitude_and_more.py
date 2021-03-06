# Generated by Django 4.0.1 on 2022-01-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='pic_url',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
