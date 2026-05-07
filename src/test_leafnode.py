import unittest
from htmlnode import LeafNode

class test_leaf_node(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_p2(self):
        node = LeafNode("div", "This is a div.", {"color" : "white", "font-size" : "15px"})
        self.assertEqual(node.to_html(), f'<div color="white" font-size="15px">This is a div.</div>')
    
    def test_leaf_to_html_p3(self):
        node = LeafNode(None, "No tag here")
        self.assertEqual(node.to_html(), "No tag here")
    
    def test_leaf_to_html_p4(self):
        node = LeafNode("p" ,  value = None)
        with self.assertRaises(ValueError):
            node.to_html()



if __name__ == "__main__":
    unittest.main()