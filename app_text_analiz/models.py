from django.db import models
class Analiz_one_dok(models.Model):
    words=models.JSONField(default=dict,unique=True)
class Analiz_doks(models.Model):
    dic_words=models.JSONField(default=dict)
