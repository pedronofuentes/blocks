from django import template
from blocks.block_library import BlockLibrary, NotInLibraryException

register = template.Library()


@register.simple_tag
def get_block(block_name):
    block_library = BlockLibrary()
    block_library.autodiscover()
    try:
        return block_library.get_block(block_name)()
    except NotInLibraryException:
        return ''