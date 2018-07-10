from django.db import models


class HallModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Залы"


class ExhibitModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    epoch = models.CharField(max_length=32)
    country = models.CharField(max_length=2)
    hall = models.ForeignKey(HallModel, related_name="exhibits", on_delete="RESTRICT")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Экспонат"
        verbose_name_plural = "Экспонаты"


class PictureModel(models.Model):
    image = models.ImageField()
    exhibit = models.ForeignKey(ExhibitModel, related_name="images", on_delete="NULL")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
