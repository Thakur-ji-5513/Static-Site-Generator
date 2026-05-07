import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode, ParentNode

class test_text_node_to_html(unittest.TestCase):
    def test_1(self):
        node = TextNode("this is supposed to be bold.", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<b>this is supposed to be bold.</b>")

    def test_2(self):
        node = TextNode("google", TextType.IMAGE,"www.goggle.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), f'<img src="www.goggle.com" alt="google"></img>')

    def test_3(self):
        node = TextNode("this is wrong", TextType.TEXT)
        node.text_type = "invalid"  # override with something not in the enum
        with self.assertRaises(Exception):
            text_node_to_html_node(node)
   

if __name__ == "__main__" :
    unittest.main()