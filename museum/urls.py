from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^halls/(\d+)/$', views.hall, name='hall'),
    path('propose/', views.propose, name='propose'),
    path('halls/', views.hall_list, name='hall_list')
]
