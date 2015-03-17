import csv
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from .models import Record
from .exporters import (
    Record1FieldExporter,
    RecordExcludeIdExporter,
    RecordFieldAndExcludeExporter,
    RecordDynamicExporter
)


class FieldAccessibility(TestCase):
    record = None

    def setUp(self):
        self.record = Record(title="Hello").save()

    def test_fields(self):
        records = Record.objects.all()
        exporter = Record1FieldExporter(queryset=records)
        io_file = exporter.to_file(StringIO())

        formatted_csv = csv_to_dict(io_file)
        size = len(list(enumerate(formatted_csv[0])))
        self.assertEquals(size, 1)

    def test_exclude(self):
        records = Record.objects.all()
        exporter = RecordExcludeIdExporter(queryset=records)
        io_file = exporter.to_file(StringIO())

        formatted_csv = csv_to_dict(io_file)
        size = len(list(enumerate(formatted_csv[0])))
        self.assertEquals(size, 4)

    def test_fields_and_exclude(self):
        records = Record.objects.all()
        exporter = RecordFieldAndExcludeExporter(queryset=records)
        io_file = exporter.to_file(StringIO())

        formatted_csv = csv_to_dict(io_file)
        size = len(list(enumerate(formatted_csv[0])))
        self.assertEquals(size, 2)

    def test_dynamic_exporter(self):
        records = Record.objects.all()
        exporter = RecordDynamicExporter(queryset=records)
        io_file = exporter.to_file(StringIO())

        formatted_csv = csv_to_dict(io_file)
        self.assertTrue("alt_title" in formatted_csv[0])


class ViewTestCase(TestCase):
    def setUp(self):
        self.record = Record(title="Hello").save()

    def test_render(self):
        path = reverse('csv_view')

        c = Client()
        r = c.get(path)
        self.assertEquals(r.status_code, 200)
        result_dict = csv_to_dict(StringIO(r.content))

        self.assertFalse("id" in result_dict[0])


def csv_to_dict(csvfile):
    rows = []

    val = csvfile.getvalue().strip("\r\n")
    csvfile = StringIO(val)

    reader = csv.DictReader(csvfile)
    for row in reader:
        rows.append(row)

    return rows
