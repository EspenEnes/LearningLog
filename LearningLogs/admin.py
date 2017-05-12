# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from LearningLogs.models import Topic,Entry, Comments

# Register your models here.

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Comments)