from django.test import TestCase
from blocks import BlockLibrary, NotInLibraryException


def foo_block():
    pass


def another_foo_block():
    pass


class BlockLibraryTest(TestCase):
    def setUp(self):
        self.block_library = BlockLibrary()

    def tearDown(self):
        self.block_library.remove_all_blocks()

    def test_add_block(self):
        """
        Tests that BlockLibrary adds block
        """
        self.block_library.add_block(foo_block)
        self.assertEqual(len(self.block_library.get_blocks()), 1, 'Number of blocks in library shoud be 1')
        self.assertIn('blocks.tests.foo_block', self.block_library.get_blocks(), 'blocks.tests.foo_block key should be in the library dictionary')

    def test_get_block(self):
        """
        Tests that BlockLibrary returns selected block
        """
        self.block_library.add_block(foo_block)
        self.assertEqual(len(self.block_library.get_blocks()), 1, 'Number of blocks in library shoud be 1')
        self.assertIn('blocks.tests.foo_block', self.block_library.get_blocks(), 'blocks.tests.foo_block key should be in the library dictionary')
        self.assertIn('__call__', dir(self.block_library.get_block('blocks.tests.foo_block')), 'BlockLibrary.get_block should return a function')
        self.assertIs(self.block_library.get_block('blocks.tests.foo_block'), foo_block, 'BlockLibrary.get_block should return foo_block')

    def test_get_blocks(self):
        """
        Tests that BlockLibrary returns the library
        """
        self.block_library.add_block(foo_block)
        self.block_library.add_block(another_foo_block)
        the_library = self.block_library.get_blocks()
        self.assertEqual(len(the_library), 2, 'the_library length shoud be 2')
        self.assertIn('blocks.tests.foo_block', the_library, 'blocks.tests.foo should be in the_library')
        self.assertIn('blocks.tests.another_foo_block', the_library, 'blocks.tests.another_foo_block should be in the_library')

    def test_get_block_not_in_library(self):
        """
        Tests that if given block is not in the library raises a NotInLibraryException
        """
        self.assertRaisesRegexp(NotInLibraryException, 'foo.blocks.a_block is not in the library', self.block_library.get_block, 'foo.blocks.a_block')

    def test_remove_all_blocks(self):
        """
        Tests that BlockLibrary removes all blocks
        """
        self.block_library.add_block(foo_block)
        self.block_library.add_block(another_foo_block)
        self.assertEqual(len(self.block_library.get_blocks()), 2, 'Number of blocks in the library shoud be 2')
        self.assertIn('blocks.tests.foo_block', self.block_library.get_blocks(), 'blocks.tests.foo_block key should be in the library dictionary')
        self.assertIn('blocks.tests.another_foo_block', self.block_library.get_blocks(), 'blocks.tests.another_foo_block key should be in the library dictionary')
        self.block_library.remove_all_blocks()
        self.assertEqual(len(self.block_library.get_blocks()), 0, 'Number of blocks in the library should be 0')

    def test_remove_block(self):
        """
        Tests that BlockLibrary removes a block
        """
        self.block_library.add_block(foo_block)
        self.block_library.add_block(another_foo_block)
        self.assertEqual(len(self.block_library.get_blocks()), 2, 'Number of blocks in the library shoud be 2')
        self.assertIn('blocks.tests.foo_block', self.block_library.get_blocks(), 'blocks.tests.foo_block key should be in the library dictionary')
        self.assertIn('blocks.tests.another_foo_block', self.block_library.get_blocks(), 'blocks.tests.another_foo_block key should be in the library dictionary')
        self.block_library.remove_block('blocks.tests.another_foo_block')
        self.assertNotIn('blocks.tests.another_foo_block', self.block_library.get_blocks(), 'blocks.tests.another_foo_block should not be in the library dictionary')

    def test_remove_block_not_in_library(self):
        """
        Tests that if the block wanted to remove is not in the library raises a NotInLibraryException
        """
        self.assertRaisesRegexp(NotInLibraryException, 'foo.blocks.a_block is not in the library', self.block_library.remove_block, 'foo.blocks.a_block')
