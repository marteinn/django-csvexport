#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
csvexport.shortcuts
-------------------------
Contains django view shortcuts
"""

from django.http import HttpResponse


def render_to_csv(exporter, filename=None):
    """
    Helper that generates a downloadable csv based on exporter,
    similar to django.shortcuts.render_to_response

    :param exporter: ModelExporter that csv will be based on.
    :param filename: The name the generated file will recive.

    Usage:

        url(r'^csv/$', 'app.views.gen_csv'),


    ... In views.py

        def gen_csv(request):
            from csvexport.exporters import ModelExporter
            from csvexport.utils import render_to_csv

            records = Record.objects.all()
            exp = ModelExporter(queryset=records)
            return render_to_csv(exp)

    """

    if not filename:
        import uuid

        token = uuid.uuid4()
        token = str(token).replace("-", "")
        filename = "%s.csv" % token

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=%s" % filename
    exporter.to_file(response)

    return response
