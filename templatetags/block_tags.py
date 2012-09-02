from django import template
from blocks.block_library import BlockLibrary, NotInLibraryException

register = template.Library()


@register.tag
def get_block(parser, token):
    try:
        elements = token.split_contents()
        tag_name = elements[0]
        arguments = elements[1:]
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    if len(arguments) > 2:
        raise template.TemplateSyntaxError("%r tag takes as much 2 arguments" % tag_name)
    return BlockNode(arguments)


class BlockNode(template.Node):
    def __init__(self, arguments):
        self.block_library = BlockLibrary()
        self.block_library.autodiscover()
        self.block_name = arguments[0][1:-1]
        self.argument = arguments[1][1:-1] if len(arguments) > 1 else None

    def render(self, context):
        try:
            block = self.block_library.get_block(self.block_name)
        except NotInLibraryException:
            return ''
        if not self.argument:
            return block()
        else:
            return block(self.argument)


@register.simple_tag
def get_block_with_arg(block_name, arg):
    block_library = BlockLibrary()
    block_library.autodiscover()
    try:
        return block_library.get_block(block_name)(arg)
    except NotInLibraryException:
        return ''
