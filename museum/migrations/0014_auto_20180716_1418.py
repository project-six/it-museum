# Generated by Django 2.0.7 on 2018-07-16 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0013_picture_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exhibit',
            name='order_number',
        ),
        migrations.AddField(
            model_name='exhibit',
            name='order_year',
            field=models.IntegerField(default=1, verbose_name='год (для сортировки)'),
            preserve_default=False,
        ),
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
    ]