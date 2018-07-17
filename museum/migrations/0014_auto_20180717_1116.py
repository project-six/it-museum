# Generated by Django 2.0.7 on 2018-07-17 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0013_picture_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibit',
            name='country',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='код страны'),
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='epoch',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='год(-ы)'),
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='order_number',
            field=models.IntegerField(verbose_name='год (для сортировки)'),
        ),
    ]