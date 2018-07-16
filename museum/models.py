from django.db import models
from django.utils import timezone


class Hall(models.Model):
    number = models.IntegerField(verbose_name="номер", unique=True)
    name = models.CharField(max_length=100, verbose_name="название", null=False)
    epoch = models.CharField(max_length=50, verbose_name="эпоха", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "зал"
        verbose_name_plural = "залы"


class Exhibit(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    order_number = models.IntegerField(verbose_name="порядковый номер")
    epoch = models.CharField(max_length=32, verbose_name="год(-ы)", null=True, blank=True)
    country = models.CharField(max_length=2, verbose_name="страна", null=True, blank=True)
    hall = models.ForeignKey(Hall, related_name="exhibits", on_delete="RESTRICT", verbose_name="зал")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "экспонат"
        verbose_name_plural = "экспонаты"


class Picture(models.Model):
    image = models.ImageField(upload_to='img', verbose_name="изображение")
    exhibit = models.ForeignKey(Exhibit, related_name="images", on_delete="NULL", verbose_name="экспонат")

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "изображения"


class Proposal(models.Model):
    name = models.CharField(max_length=50, verbose_name="имя отправителя", blank=False, null=False)
    email = models.EmailField(verbose_name="E-Mail", blank=True, null=True)
    message = models.TextField(verbose_name="описание")
    sent = models.DateTimeField(default=timezone.now, verbose_name="дата")

    class Meta:
        verbose_name = "предлагаемый экспонат"
        verbose_name_plural = "предлагаемые экспонаты"
