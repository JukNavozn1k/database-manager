# Generated by Django 5.0.4 on 2024-04-06 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_manager', '0004_alter_category_description_alter_category_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]
