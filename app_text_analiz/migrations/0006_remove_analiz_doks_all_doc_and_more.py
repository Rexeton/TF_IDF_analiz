# Generated by Django 4.2.5 on 2024-04-16 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_text_analiz', '0005_alter_analiz_doks_all_doc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analiz_doks',
            name='all_doc',
        ),
        migrations.AlterField(
            model_name='analiz_doks',
            name='dic_words',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='analiz_one_dok',
            name='words',
            field=models.JSONField(default=dict, unique=True),
        ),
    ]