import unittest
from functions import split_nodes_delimiter
from textnode import TextNode,TextType

class test_split(unittest.TestCase):
    def test_case1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes,[TextNode("This is text with a ", TextType.TEXT),TextNode("code block", TextType.CODE),TextNode(" word", TextType.TEXT),])


    def test_case2(self):
        node = TextNode("This is text with a `code block' word", TextType.TEXT)
        with self.assertRaises(Exception):
            new_node = split_nodes_delimiter([node],"'", TextType.CODE)



if __name__ == "__main__":
    unittest.main()