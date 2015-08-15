from csvexport.exporters import ModelExporter


class Record1FieldExporter(ModelExporter):
    class Meta:
        fields = ["title"]


class RecordExcludeIdExporter(ModelExporter):
    class Meta:
        exclude = ["id"]


class RecordFieldAndExcludeExporter(ModelExporter):
    class Meta:
        fields = ["rank", "title", "id"]
        exclude = ["id"]


class RecordDynamicExporter(ModelExporter):
    class Meta:
        fields = ["alt_title"]

    @staticmethod
    def hydrate_entry(entry):
        dict_entry = {}
        dict_entry["alt_title"] = entry.title
        return dict_entry
