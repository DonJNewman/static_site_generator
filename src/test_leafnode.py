import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        return self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_LINK(self):
        node = LeafNode("a", "scoobydoo!", {"href": "https://google.com"})
        self.assertEqual(node.to_html(), '<a href="https://google.com">scoobydoo!</a>')
        return self.assertEqual(node.to_html(), '<a href="https://google.com">scoobydoo!</a>')
    
    def test_bold_phont(self):
        node = LeafNode("b", "scoobydoo!", {"href": "https://google.com"})
        expected_output = '<b href="https://google.com">scoobydoo!</b>'
        self.assertEqual(node.to_html(), expected_output)

    def test_no_value(self):
        node = LeafNode("p", None)
        self.assertEqual(node.to_html(), None)
        return self.assertNotEqual(node.to_html(), ValueError)        




if __name__ == "__main__":
    unittest.main()


