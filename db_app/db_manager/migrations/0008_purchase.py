# Generated by Django 5.0.4 on 2024-04-07 23:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_manager', '0007_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='db_manager.customer', verbose_name='Покупатель')),
                ('good', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='db_manager.good', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Покупка',
                'verbose_name_plural': 'Покупки',
            },
        ),
    ]
