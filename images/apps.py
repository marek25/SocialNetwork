# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class ImagesConfig(AppConfig):
    name = 'images'
    verbose_name = 'Image bookmarks'

    #fali joj verbose_name

    def ready(self):
    	#import signal handlers
    	import images.signals
