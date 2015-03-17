from django.db import models


class Parent(models.Model):
    title = models.CharField(max_length=30)


class Record(models.Model):
    parent = models.ForeignKey(Parent, blank=True, null=True)
    title = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    rank = models.IntegerField(default=0, blank=True)
