from django.db import models

class Entity(models.Model):
    date_type_text = models.DateField(null=True)
    date_type_date = models.DateField(null=True)
