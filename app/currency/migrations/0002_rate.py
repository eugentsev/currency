# Generated by Django 3.2.5 on 2021-07-27 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale', models.DecimalField(decimal_places=2, max_digits=5)),
                ('buy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('source', models.CharField(max_length=32)),
                ('type', models.CharField(max_length=3)),
            ],
        ),
    ]
