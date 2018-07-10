from django.contrib import admin

from .models import HallModel, ExhibitModel, PictureModel

admin.site.register(HallModel)
admin.site.register(ExhibitModel)
admin.site.register(PictureModel)
