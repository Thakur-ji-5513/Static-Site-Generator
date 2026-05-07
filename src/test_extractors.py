import unittest
from functions import extract_markdown_images,extract_markdown_links,split_nodes_image,split_nodes_link, text_to_textnodes, markdown_to_blocks
from textnode import TextNode,TextType

class test_extract_fnc(unittest.TestCase):
    def test_img_1(self):
            matches = extract_markdown_images(
                "This is a text without the img tag"
            )
            self.assertEqual([], matches)

    def test_img_2(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_links_1(self):
            matches = extract_markdown_links(
                "This is a text without the link tag"
            )
            self.assertEqual([], matches)

    def test_links_2(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
    
    def test_links_3(self):
        matches = extract_markdown_links(
            "This is text with a img ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([], matches)

class test_split_funcs(unittest.TestCase):
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
    )


class test_text_to_textNodes(unittest.TestCase):
    def test_1(self):
        content = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertEqual(text_to_textnodes(content),
        [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])


    def test_2(self):
        content = "simple plain text"
        self.assertEqual(text_to_textnodes(content),
        [TextNode(content, TextType.TEXT)]
        )

    def test_3(self):
        content = 'some text with a **bold** tag'
        ans = [TextNode('some text with a ', TextType.TEXT),
               TextNode('bold', TextType.BOLD),
               TextNode(' tag', TextType.TEXT)
                ]
        self.assertEqual(ans, text_to_textnodes(content))

    def test_markdown_to_blocks(self):
        md = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

if __name__ == "__main__":
    unittest.main()