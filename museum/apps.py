from watson import search as watson
from django.apps import AppConfig


class MuseumConfig(AppConfig):
    name = 'museum'
    verbose_name = "IT-Museum"

    def ready(self):
        exhibit = self.get_model('Exhibit')
        watson.register(exhibit, fields=('name', 'description'))
