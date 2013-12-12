from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)
    visible = models.BooleanField(default=False)
    publish_date = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __unicode__(self):
        return self.title

    @property
    def words(self):
        return len(self.text.split())


class Tag(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self')
