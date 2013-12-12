from django.db import models


class Link(models.Model):
    url = models.UrlField(max_length=255)
    archived_copies = models.ManyToManyField('MHTArchive')


class MHTArchive(models.Model):
    access_date = models.DateTimeField()
    mht_file = models.FileField()
