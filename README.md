[![Build Status](https://travis-ci.org/marteinn/django-csvexport.svg?branch=master)](https://travis-ci.org/marteinn/django-csvexport)

# Django-CSVExport

This is a django extension that simplifies model to csv conversions.


## Requirements
- Python 2.7
- Django 1.6+


## Example:

### Simple usage:

```python
from csvexport.exports import ModelCSVExporter

records = Record.objects.all()
exp = ModelExporter(queryset=records)
f = exp.to_string()
```

### With specified fields

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


### With custom hydration:

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


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Django-CSVExport is released under the [MIT License](http://www.opensource.org/licenses/MIT).
