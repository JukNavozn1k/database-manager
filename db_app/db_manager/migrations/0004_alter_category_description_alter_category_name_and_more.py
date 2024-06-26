# Generated by Django 5.0.4 on 2024-04-05 22:46

import db_manager.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_manager', '0003_alter_good_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=1024, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='good',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='db_manager.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='good',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='good',
            name='price',
            field=models.FloatField(validators=[db_manager.models.PositiveFloatValidator()], verbose_name='Цена'),
        ),
    ]
