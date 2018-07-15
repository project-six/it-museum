from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^halls/(\d+)/$', views.hall, name='hall'),
    path('propose/', views.propose, name='propose'),
    re_path(r'^exhibits/(\d+)/$', views.exhibit, name='exhibit')
]
