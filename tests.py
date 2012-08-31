from django.test import TestCase


def foo_block():
    pass


def another_foo_block():
    pass


class BlockLibraryTest(TestCase):
    def setUp(self):
        self.register = BlockLibrary()

    def tearDown(self):
        self.register.remove_all_blocks()

    def test_add_block(self):
        """
        Tests that BlockLibrary adds block
        """
        self.register.add_block(foo_block)
        self.assertEqual(len(self.register.get_blocks()), 1, 'Number of blocks in library shoud be 1')
        self.assertIn('blocks.tests.foo_block', self.register.get_blocks(), 'blocks.tests.foo_block key should be in the library dictionary')

    def test_get_block(self):
        """
        Tests that BlockLibrary returns selected block
        """
        self.register.add_block(foo_block)
        self.assertEqual(len(self.register.get_blocks()), 1, 'Number of blocks in library shoud be 1')
        self.assertIn('blocks.tests.foo_block', self.register.get_blocks(), 'blocks.tests.foo_block key should be in the library dictionary')
        self.assertIn('__call__', dir(self.register.get_block('blocks.tests.foo_block')), 'BlockLibrary.get_block should return a function')
        self.assertIs(self.register.get_block('blocks.tests.foo_block'), foo_block, 'BlockLibrary.get_block should return foo_block')

    def test_get_block_not_in_library(self):
        """
        Tests that if given block is not in the library raises a NotInLibraryExcetpion
        """
        self.assertRaisesRegexp(NotInLibraryExcetpion, 'foo.blocks.a_block is not in the library', self.register.get_block('foo.blocks.a_block'))

    def test_remove_all_blocks(self):
        """
        Tests that BlockLibrary removes all blocks
        """
        self.register.add_block(foo_block)
        self.register.add_block(another_foo_block)
        self.assertEqual(len(self.register.get_blocks()), 2, 'Number of blocks in the library shoud be 2')
        self.assertIn('blocks.tests.foo_block', self.register.get_blocks(), 'blocks.tests.foo_block key should be in the library dictionary')
        self.assertIn('blocks.tests.another_foo_block', self.register.get_blocks(), 'blocks.tests.another_foo_block key should be in the library dictionary')
        self.register.remove_all_blocks()
        self.assertEqual(len(self.register.get_blocks()), 0, 'Number of blocks in the library should be 0')

    def test_remove_block(self):
        """
        Tests that BlockLibrary removes a block
        """
        self.register.add_block(foo_block)
        self.register.add_block(another_foo_block)
        self.assertEqual(len(self.register.get_blocks()), 2, 'Number of blocks in the library shoud be 2')
        self.assertIn('blocks.tests.foo_block', self.register.get_blocks(), 'blocks.tests.foo_block key should be in the library dictionary')
        self.assertIn('blocks.tests.another_foo_block', self.register.get_blocks(), 'blocks.tests.another_foo_block key should be in the library dictionary')
        self.register.remove_block('blocks.tests.another_foo_block')
        self.assertNotIn('blocks.tests.another_foo_block', self.register.get_blocks(), 'blocks.tests.another_foo_block should not be in the library dictionary')

    def test_remove_block_not_in_library(self):
        """
        Tests that if the block wanted to remove is not in the library raises a NotInLibraryExcetpion
        """
        self.assertRaisesRegexp(NotInLibraryExcetpion, 'foo.blocks.a_block is not in the library', self.register.remove_block('foo.blocks.a_block'))
