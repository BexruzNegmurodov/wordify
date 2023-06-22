# Generated by Django 4.2.2 on 2023-06-14 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=221)),
                ('number', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_date', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
