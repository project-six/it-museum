from django.db import models


class Hall(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Залы"


class Exhibit(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    epoch = models.CharField(max_length=32, verbose_name="Год(-ы)")
    country = models.CharField(max_length=2, verbose_name="Страна")
    hall = models.ForeignKey(Hall, related_name="exhibits", on_delete="RESTRICT", verbose_name="Зал")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Экспонат"
        verbose_name_plural = "Экспонаты"


class Picture(models.Model):
    image = models.ImageField(verbose_name="Изображение")
    exhibit = models.ForeignKey(Exhibit, related_name="images", on_delete="NULL", verbose_name="Экспонат")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
