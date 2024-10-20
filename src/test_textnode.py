import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_TextType(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        self.assertEqual(node.text_type, "bold")
        node = TextNode("This is a bold text node", TextType.NORMAL)
        self.assertEqual(node.text_type, "normal")
        node = TextNode("This is a bold text node", TextType.ITALIC)
        self.assertEqual(node.text_type, "italic")
        node = TextNode("This is a bold text node", TextType.CODE)
        self.assertEqual(node.text_type, "code")
        node = TextNode("This is a bold text node", TextType.LINK)
        self.assertEqual(node.text_type, "link")
        node = TextNode("This is a bold text node", TextType.IMAGE)
        self.assertEqual(node.text_type, "image")
    
    def test_url(self):
        node = TextNode("This is a text node", TextType.LINK, None)
        self.assertEqual(node.url, None)
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        self.assertEqual(node.url, "https://www.google.com")
        node = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(node.url, None)
    
    def test_diff(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a different text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)

        node2 = TextNode("This is a text node", TextType.ITALIC, None)
        self.assertNotEqual(node, node2)

        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()