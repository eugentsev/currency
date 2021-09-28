# Generated by Django 3.2.5 on 2021-09-19 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_code', models.PositiveSmallIntegerField()),
                ('path', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('request_method', models.CharField(choices=[('GET', 'GET'), ('POST', 'POST')], max_length=4)),
                ('response_time', models.PositiveSmallIntegerField(help_text='in milliseconds')),
            ],
        ),
    ]
