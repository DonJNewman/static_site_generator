import unittest

from htmlnode import HTMLNode

class Testhtmlnode(unittest.TestCase):
    def test_eq(self): #TEST EQUAL
        node = HTMLNode("<p>", "This is my value (:", (HTMLNode("<h3>", "ooooo smol node", None, {"href": "https://www.google.com", "target": "_blank"})), {"href": "https://www.google.com", "target": "_blank"} )
        node2 = HTMLNode("<p>", "This is my value (:", (HTMLNode("<h3>", "ooooo smol node", None, {"href": "https://www.google.com", "target": "_blank"})), {"href": "https://www.google.com", "target": "_blank"} )
        self.assertEqual(node, node2)



    def test_not_eq_tag(self): #NOT EQUAL tag
        node = HTMLNode("<p>", "This is my value (:", (HTMLNode("<h3>", "ooooo smol node", None, {"href": "https://www.google.com", "target": "_blank"})), {"href": "https://www.google.com", "target": "_blank"} )
        node2 = HTMLNode("<h1>", "This is my value (:", (HTMLNode("<h3>", "ooooo smol node", None, {"href": "https://www.google.com", "target": "_blank"})), {"href": "https://www.google.com", "target": "_blank"} )
        self.assertNotEqual(node, node2) 


     
    def test_not_eq_value(self): #NOT EQUAL val
        node = HTMLNode("<p>", "This is my value (:", (HTMLNode("<h3>", "ooooo smol node", None, {"href": "https://www.google.com", "target": "_blank"})), {"href": "https://www.google.com", "target": "_blank"} )
        node2 = HTMLNode("<p>", "This is not my value (:", (HTMLNode("<h3>", "ooooo smol node", None, {"href": "https://www.google.com", "target": "_blank"})), {"href": "https://www.google.com", "target": "_blank"} )
        self.assertNotEqual(node, node2)    


    
    def test_not_eq_url(self): #NOT EQUAL CHILDREN
        node = HTMLNode("<p>", "This is my value (:", (HTMLNode("<h3>", "ooooo smol node", None, {"href": "https://www.google.com", "target": "_blank"})), {"href": "https://www.google.com", "target": "_blank"} )
        node2 = HTMLNode("<p>", "This is my value (:", (HTMLNode("<h3>", "ooooo smol  child altered node", None, {"href": "https://www.facebook.com", "target": "_blank"})), {"href": "https://www.google.com", "target": "_blank"} ) 
        self.assertNotEqual(node, node2)    

    def test_eq(self): #NOT EQUAL LINKS
        node = HTMLNode("<p>", "This is my value (:", (HTMLNode("<h3>", "ooooo smol node", None, {"href": "https://www.google.com", "target": "_blank"})), {"href": "https://www.facebook.com", "target": "_blank"} )
        node2 = HTMLNode("<p>", "This is my value (:", (HTMLNode("<h3>", "ooooo smol node", None, {"href": "https://www.google.com", "target": "_blank"})), {"href": "https://www.google.com", "target": "_blank"} )
        self.assertNotEqual(node, node2)

    


if __name__ == "__main__":
    unittest.main()
