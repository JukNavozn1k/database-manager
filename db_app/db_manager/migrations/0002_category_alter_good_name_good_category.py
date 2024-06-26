# Generated by Django 5.0.4 on 2024-04-05 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.CharField(max_length=1024)),
            ],
        ),
        migrations.AlterField(
            model_name='good',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AddField(
            model_name='good',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='db_manager.category'),
        ),
    ]
