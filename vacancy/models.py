from django.db import models

# Create your models here.
class TopSkills(models.Model):
    name = models.CharField(max_length=40)
    year = models.IntegerField()
    is_profession = models.BooleanField()
    chart = models.FileField(upload_to="topskills")
class GeographySalary(models.Model):
    salary = models.IntegerField()
    area_name = models.CharField(max_length=40)
    fraction = models.FloatField()
    is_profession = models.BooleanField()
class RelevanceSalary(models.Model):
    salary = models.IntegerField()
    counter = models.IntegerField()
    year = models.IntegerField()
    is_profession = models.BooleanField()

class MainPage(models.Model):
    header = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    image = models.FileField()
    is_set = models.BooleanField()

