# Generated by Django 4.2.5 on 2024-04-16 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_text_analiz', '0004_analiz_doks_all_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analiz_doks',
            name='all_doc',
            field=models.BigIntegerField(default=0),
        ),
    ]
