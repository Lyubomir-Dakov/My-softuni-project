# Generated by Django 3.2.16 on 2022-12-03 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_carcomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carcomment',
            options={'ordering': ['publication_date_and_time']},
        ),
    ]