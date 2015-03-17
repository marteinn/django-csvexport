from csvexport.shortcuts import render_to_csv
from .exporters import (
    RecordExcludeIdExporter,
)
from .models import Record


def csv_view(request, *args, **kwargs):
    records = Record.objects.all()
    exporter = RecordExcludeIdExporter(queryset=records)

    return render_to_csv(exporter)

