# Generated by Django 4.2.5 on 2023-10-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.TextField(max_length=6, unique=True)),
                ('long_url', models.TextField(max_length=100, unique=True)),
            ],
        ),
    ]
