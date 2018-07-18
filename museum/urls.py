from django.urls import path, re_path

from museum import views

urlpatterns = [
    path('', views.index, name='index'),
    path('halls/', views.hall_list, name='hall_list'),
    re_path(r'^halls/(?P<hall_number>\d+)(?:/exhibit/(?P<exh_id>\d+))?/$', views.hall, name='hall'),
    re_path(r'^exhibit_data/(\d+)/$', views.exhibit_data, name='exhibit_data'),
    path('propose/', views.propose, name='propose'),
    path('search/', views.search, name='search'),
    path('random/', views.random_exh, name='random')
]
