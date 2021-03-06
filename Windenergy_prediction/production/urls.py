from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('main', views.main, name="main"),
    path('map', views.map, name="map"),
    path('add_location_map', views.add_location_map, name="add_location_map"),
    path('update_profile', views.update_profile, name="update_profile"),
    path('comp_analysis', views.comp_analysis, name='comp_analysis'),
    path('windform_location', views.windform_location, name="windform_location"),
    path('logout', views.logout, name="logout"),
    path('map_display',views.map_display, name="map_display"),
    path('upload',views.upload,name="upload"),
    path('direct',views.direct,name="direct"),
    path('show_analysis',views.show_analysis,name='show_analysis'),
    path('show_graph',views.show_graph,name="show_graph"),
    path('my_home', views.my_home, name="my_home"),
    #path('show_predict_values',views.show_predict_values,name="show_predict_values"),
]
