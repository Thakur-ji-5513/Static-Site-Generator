from Block import BlockType, block_to_block_type
import unittest


class test_block_to_block_type(unittest.TestCase):
    def test_1(self):
        content = "just some good ol plain text"
        node = block_to_block_type(content)
        self.assertEqual(node, BlockType.PARA)

    def test_2(self):
        content = "## Heading 2 ##"
        node = block_to_block_type(content)
        self.assertEqual(node, BlockType.HEADING)

    def test_3(self):
        content = "```\nsome randon code```"
        node = block_to_block_type(content)
        self.assertEqual(node, BlockType.CODE)
    
    def test_4(self):
        content = "- item one\n- item two\nnot a list item"
        node = block_to_block_type(content)
        self.assertEqual(node, BlockType.PARA)


if __name__ == "__main__":
    unittest.main()
