# Generated by Django 3.2.20 on 2023-09-03 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0003_material_material_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
