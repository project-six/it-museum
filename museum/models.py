from django.db import models


class HallModel(models.Model):
    name = models.CharField(max_length=100)


class ExhibitModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    hall = models.ForeignKey(HallModel, related_name="exhibits", on_delete="RESTRICT")


class PictureModel(models.Model):
    image = models.ImageField()
    exhibit = models.ForeignKey(ExhibitModel, related_name="images", on_delete="NULL")
