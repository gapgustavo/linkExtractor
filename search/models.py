from django.db import models

# Create your models here.
class Search(models.Model):
    link = models.CharField(max_length=300)
    links_list = models.JSONField()
    date = models.DateField()