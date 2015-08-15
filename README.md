[![Build Status](https://travis-ci.org/marteinn/django-csvexport.svg?branch=master)](https://travis-ci.org/marteinn/django-csvexport)
[![PyPI version](https://badge.fury.io/py/django-csvexport.svg)](http://badge.fury.io/py/django-csvexport)

# Django-CSVExport

This is a django extension that simplifies model to csv conversions.


## Requirements
- Python 2.7 / 3.2+
- Django 1.6+


## Example:

### Simple usage:

Generate csv string from a model:

```python
from csvexport.exports import ModelCSVExporter

records = Record.objects.all()
exp = ModelExporter(queryset=records)
f = exp.to_string()
```

### With specified fields

Same as the previous example, but only expose certain fields:

```python
from csvexport.exports import ModelCSVExporter

class RecordExporter(ModelCSVExporter):
    class Meta:
        fields = ["album", "slug"]
        exclude = ["id"]


records = Record.objects.all()
exp = RecordExporter(queryset=records)
f = exp.to_string()
```

### Generating a csv from a view:

This is a example how you could generate a downloadable csv by requesting a view, using the `render_to_csv` helper.

**urls.py**

```python
url(r'^csv/$', 'app.views.gen_csv'),
```

**views.py**

```python
def gen_csv(request):
    from csvexport.exporters import ModelExporter
    from csvexport.utils import render_to_csv
    records = Record.objects.all()
    exp = ModelExporter(queryset=records)
    return render_to_csv(exp)
```

### With custom hydration

It is also possible to create a custom csv object:

```python
class RecordExporter(ModelExporter):
    class Meta:
        fields = ["artist", "title", "release_year", "format", "quality",
                  "record_label", "comment", "venue", "url"]

    def hydrate_entry(self, entry):
        venue_name = ""

        if entry.venue:
            venue_name = entry.venue.name

        return {
            "artist": entry.album.artist.name,
            "title": entry.album.name,
            "release_year": entry.album.release_year,
            "format": entry.format,
            "quality": entry.quality,
            "record_label": entry.record_label,
            "comment": entry.comment,
            "venue": venue_name,
        }


records = Record.objects.all()
exp = RecordExporter(queryset=records)
f = exp.to_string()

```


## Installation

Genres can easily be installed through pip.

    $ pip install django-csvexport


## Tests

This library include tests, just run `python runtests.py`.

You can also run separate test cases: `runtests.py tests.ViewTestCase`


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Django-CSVExport is released under the [MIT License](http://www.opensource.org/licenses/MIT).
