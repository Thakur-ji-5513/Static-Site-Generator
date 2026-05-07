import unittest

from htmlnode import HTMLNode

class test_html_node(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode("h1", "this is a h1 tag", [], {"font-size":'20px'})
        self.assertEqual(node.props_to_html(), ' font-size="20px"')

    def test_props_to_html2(self):
        node = HTMLNode("h1", "this is a h1 tag", [], {})
        self.assertEqual(node.props_to_html(), '')


if __name__ == "__main__":
    unittest.main()