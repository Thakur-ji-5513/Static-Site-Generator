import unittest
from htmlnode import ParentNode,LeafNode

class test_Parent_node(unittest.TestCase):
    def test_leaf_to_html(self):
        child_node = LeafNode("p","child p")
        parent_node = ParentNode("div",children=[child_node])
        self.assertEqual(parent_node.to_html(), "<div><p>child p</p></div>")

    def test_leaf_to_html2(self):
        child_node = LeafNode("p","child")
        child_node2 = LeafNode("b","p")
        parent_node = ParentNode("div",children=[child_node,child_node2])
        self.assertEqual(parent_node.to_html(), "<div><p>child</p><b>p</b></div>")

    def test_leaf_to_html3(self):
        child_node = LeafNode("p","child p")
        parent_node = ParentNode(tag = None,children=[child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_leaf_to_html4(self):
        parent_node = ParentNode("div",children = None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()