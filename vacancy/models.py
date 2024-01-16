from django.db import models

# Create your models here.
class TopSkills(models.Model):
    name = models.CharField(max_length=40)
    year = models.IntegerField()
    is_profession = models.BooleanField()
    chart = models.FileField(upload_to="topskills")
