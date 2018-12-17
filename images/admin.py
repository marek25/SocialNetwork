# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Image

#@admin.register(Image) #dodato
class ImageAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'image', 'created']
	list_filter = ['created']


# ovo nema kod praju, vec ona gore funkcija
admin.site.register(Image, ImageAdmin)	


