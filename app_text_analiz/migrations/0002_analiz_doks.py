# Generated by Django 4.2.5 on 2024-04-15 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_text_analiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analiz_doks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words', models.JSONField(default=dict, unique=True, verbose_name='Словарь всех слов с кол-вом документов с этим словом')),
            ],
        ),
    ]
