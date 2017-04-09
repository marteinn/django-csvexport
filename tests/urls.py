from django.conf.urls import include, url

from .views import csv_view


urlpatterns = [
    url(r"^test/csv_view", csv_view, name="csv_view"),
]
