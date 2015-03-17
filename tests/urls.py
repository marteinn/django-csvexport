from django.conf.urls import patterns, include, url
from .views import csv_view


urlpatterns = patterns("",
    url(r"^test/csv_view", csv_view, name="csv_view"),
)
