# Generated by Django 4.0.10 on 2023-08-25 17:51

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326),
        ),
    ]
