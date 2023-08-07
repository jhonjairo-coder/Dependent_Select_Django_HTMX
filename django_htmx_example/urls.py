from django.contrib import admin
from django.urls import path
from example import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("load_cities/", views.load_cities, name="load_cities")
]