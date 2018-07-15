from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('halls/', views.hall_list, name='hall_list'),
    re_path(r'^halls/(\d+)/$', views.hall, name='hall'),
    re_path(r'^exhibits/(\d+)/$', views.exhibit, name='exhibit'),
    path('propose/', views.propose, name='propose')
]
