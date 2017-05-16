# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200)
    slug = models.SlugField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)
        super(Topic, self).save(*args, **kwargs)




    def __unicode__(self):
        return self.text


class Comments(models.Model):
    owner = models.ForeignKey(User)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    entry = models.ForeignKey("LearningLogs.Entry")

    class Meta:
        ordering = ['-date_added']

    def __unicode__(self):
        return self.text




class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'entries'

    def __unicode__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."



