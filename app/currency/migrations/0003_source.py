# Generated by Django 3.2.5 on 2021-07-29 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_url', models.CharField(max_length=225)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
    ]