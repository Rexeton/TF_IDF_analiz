# Generated by Django 4.2.5 on 2024-04-15 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analiz_one_dok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words', models.JSONField(default=dict, unique=True, verbose_name='Словарь из слов в одном документе')),
            ],
        ),
    ]
