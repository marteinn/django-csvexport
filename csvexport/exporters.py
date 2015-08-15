#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
csvexport.exporters
-------------------------
This module contains the basic exporter, you can either extend upon it to
make custom exports or just it as it is.
"""

import csv
try:
    from StringIO import StringIO   # Python 2.x
except ImportError:
    from io import StringIO         # Python 3.x

try:
    basestring
except NameError:
    basestring = str


class ModelExporter(object):
    """
    Simple usage:

        from csvexport.exports import ModelExporter

        records = Record.objects.all()[:5]
        exp = ModelExporter(queryset=records)
        f = exp.to_string()


    ...With specified fields

        from csvexport.exports import ModelCSVExporter

        class RecordExporter(ModelCSVExporter):
            class Meta:
                fields = ["album", "slug"]
                exclude = []


        records = Record.objects.all()[:5]
        exp = RecordExporter(queryset=records)
        f = exp.to_string()

    """

    queryset = None
    fields = None

    def __init__(self, queryset):
        """
        Exporter constructor

        :param queryset: The queryset to base the export on.

        Usage:

            >>> records = Record.objects.all()
            >>> exp = ModelExporter(queryset=records)
            >>> exp.to_string()

            artist,album
            Bowie,Lodger
            Bowie,Low

        """

        self.queryset = queryset

        try:
            self.fields = self.Meta.fields
        except AttributeError:
            self.fields = self._get_fieldnames()

        try:
            for field in self.Meta.exclude:
                self.fields.remove(field)
        except AttributeError:
            pass

    def to_string(self):
        """
        Returns csv output as a string using StringIO
        """

        cvsfile = self.to_file(StringIO())
        return cvsfile.getvalue()

    def to_file(self, csvfile, *args, **kwargs):
        """
        Writes content to file with DictWriter
        """

        writer = csv.DictWriter(csvfile, fieldnames=self.fields)
        writer.writeheader()

        for entry in self.queryset:
            parsed_entry = self.hydrate_entry(entry)
            parsed_entry = self.encode_entry(parsed_entry)

            writer.writerow(parsed_entry)

        return csvfile

    def _get_fieldnames(self):
        """
        Build array with fieldnames usting _meta.fields. Are not used when
        Meta.fields is specified
        """

        fields = [field.name for field in self.queryset.model._meta.fields]
        return fields

    def hydrate_entry(self, entry):
        """
        Iterates through model using self.fields and performs a basic model
        to dict conversion.
        """

        entry_dict = {}
        for key in self.fields:
            field = getattr(entry, key)
            if field is None:
                field = ""

            entry_dict[key] = field

        return entry_dict

    @staticmethod
    def encode_entry(dict_data):
        """
        Makes sure all items in dict are encode safe (since csv writer does
        not offer that)
        """

        formatted_data = {}
        for key, value in dict_data.items():
            value = value if value else ""
            if isinstance(value, basestring):
                value = value.encode("utf-8")

            formatted_data[key] = value

        return formatted_data
