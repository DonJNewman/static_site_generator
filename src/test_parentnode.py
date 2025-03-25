import unittest

from parentnode import ParentNode
from leafnode import LeafNode
class TestParentNode(unittest.TestCase):
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


    def test_parent_for_empty_children(self): #test for empty children
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_parent_for_valid_children(self): #test for valid children
        with self.assertRaises(TypeError):
            ParentNode("div", ["invalid child"]).to_html()
            raise TypeError('invalid child')
        
    def test_ultra_nesting(self):
        great_grandchild = LeafNode("strong", "Great-Grandchild is here")
        grandchild = ParentNode("b",[great_grandchild])
        child_node =ParentNode("span",[grandchild])
        parent_node =ParentNode("div",[child_node])
        self.assertEqual(parent_node.to_html(),
                    "<div><span><b><strong>Great-Grandchild is here</strong></b></span></div>"

                          )
    def test_missing_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span","child")])

    def test_missing_children(self):
        with self.assertRaises(ValueError, msg="ParentNode must have children"):
            ParentNode("div", None)  # Providing `None` as children
    def test_with_props(self):
    # Pass a valid child and props
        child_node = LeafNode("a", "click here")
        parent_node = ParentNode("div", [child_node], {"href": "www.google.com"})
        
        # Ensure props are added to the HTML
        self.assertEqual(
            parent_node.to_html(),
            '<div href="www.google.com"><a>click here</a></div>'
        )
if __name__ == "__main__":
    unittest.main()
