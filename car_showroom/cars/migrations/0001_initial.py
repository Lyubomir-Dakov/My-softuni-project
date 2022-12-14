# Generated by Django 3.2.16 on 2022-11-30 02:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Sports Car', 'Sports Car'), ('Pickup', 'Pickup'), ('Crossover', 'Crossover'), ('Other', 'Other')], max_length=20)),
                ('model', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)])),
                ('year_of_production', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1980, message='This car is too old!')], verbose_name='Year of production')),
                ('image_url', models.URLField(verbose_name='Image URL')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(30000, message='This car is too cheap to stay in the showroom!')])),
                ('horse_power', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(100, message='This car is too weak to stay in the showroom!')], verbose_name='Horse Power')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
