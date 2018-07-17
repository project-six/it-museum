from django.contrib import admin

from .models import Hall, Exhibit, Picture, Proposal

admin.site.register(Hall)
admin.site.register(Exhibit)
admin.site.register(Picture)
admin.site.register(Proposal)
