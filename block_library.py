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
