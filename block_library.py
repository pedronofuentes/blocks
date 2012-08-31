import re
import os
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module

block_library = {}


class NotInLibraryException(Exception):
    pass


class BlockLibrary():
    """Manages block_library"""

    def add_block(self, block):
        block_library['%s.%s' % (block.__module__, block.__name__)] = block

    def get_block(self, block):
        try:
            return block_library[block]
        except KeyError:
            raise NotInLibraryException('%s is not in the library' % block)

    def get_blocks(self):
        return block_library

    def remove_block(self, block):
        try:
            del block_library[block]
        except KeyError:
            raise NotInLibraryException('%s is not in the library' % block)

    def remove_all_blocks(self):
        for key in block_library.keys():
            del block_library[key]

    def autodiscover(self, apps=settings.INSTALLED_APPS):
        for app in apps:
            if not re.match('[django.*|blocks]', app):
                try:
                    mod = import_module(app)
                except ImportError as e:
                    raise ImproperlyConfigured('ImportError %s: %s' % (app, e.args[0]))
                if os.path.isfile(os.path.join(os.path.dirname(mod.__file__), 'blocks.py')):
                    block_module = import_module('%s.%s' % (app, 'blocks'))
                    for x in dir(block_module):
                        if callable(getattr(block_module, x)) and re.match(r'.*_block', x):
                            self.add_block(getattr(block_module, x))
