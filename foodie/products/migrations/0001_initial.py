# Generated by Django 4.0.10 on 2023-06-20 21:34

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=500)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('featured', models.BooleanField(default=False)),
                ('category', models.CharField(default='general', max_length=120)),
                ('quantity', models.IntegerField(default=1)),
                ('image', models.ImageField(upload_to='products/')),
                ('pick_up_time', models.DateTimeField(blank=True, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('number_of_days_listed', models.IntegerField(default=14)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
