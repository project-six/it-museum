# Generated by Django 2.0.7 on 2018-07-11 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exhibitmodel',
            name='hall',
        ),
        migrations.RemoveField(
            model_name='picturemodel',
            name='exhibit',
        ),
        migrations.DeleteModel(
            name='ExhibitModel',
        ),
        migrations.DeleteModel(
            name='HallModel',
        ),
        migrations.DeleteModel(
            name='PictureModel',
        ),
    ]