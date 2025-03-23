import unittest

from htmlnode import HTMLNode

class Testhtmlnode(unittest.TestCase):
    def test_eq(self): #TEST EQUAL
   
        node = HTMLNode("<p>", "This is my value (:", (HTMLNode("<h3>", "ooooo smol node", None, {"href": "https://www.google.com", "target": "_blank"})), {"href": "https://www.google.com", "target": "_blank"} )
        node2 = HTMLNode("<p>", "This is my value (:", (HTMLNode("<h3>", "ooooo smol node", None, {"href": "https://www.google.com", "target": "_blank"})), {"href": "https://www.google.com", "target": "_blank"} )
        print(f"EQComparing tag: {node.tag} == {node2.tag} : { node.tag == node2.tag }")
        print(f"EQomparing value: {node.value} == {node2.value} : {node.value == node2.value}")
        print(f"EQComparing children: {node.children} == {node2.children} : {node.children == node2.children}")
        print(f"EQComparing props: {node.props} == {node2.props} : {node.props == node2.props }")
        print(f'guy cmon wat ??????? {node.children.tag} == {node2.children.tag} : {node.children.tag == node2.children.tag}')
        print(f'guy cmon wat ??????? {node.children.value} == {node2.children.value} : {node.children.value == node2.children.value}')
        print(f'guy cmon wat ??????? {node.children.children} == {node2.children.children} : {node.children.children == node2.children.children}')
        print(f'guy cmon wat ??????? {node.children.props} == {node2.children.props} : {node.children.props== node2.children.props}')
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

    def test_not_eq_links(self): #NOT EQUAL LINKS
        node = HTMLNode("<p>", "This is my value (:", (HTMLNode("<h3>", "ooooo smol node", None, {"href": "https://www.google.com", "target": "_blank"})), {"href": "https://www.facebook.com", "target": "_blank"} )
        node2 = HTMLNode("<p>", "This is my value (:", (HTMLNode("<h3>", "ooooo smol node", None, {"href": "https://www.google.com", "target": "_blank"})), {"href": "https://www.google.com", "target": "_blank"} )
        self.assertNotEqual(node, node2)

    def test_empty_value(self): #TEST EQUAL
        node = HTMLNode("<p>", "This is my value (:", (HTMLNode("<h3>", "ooooo smol node", None, {"href": "https://www.google.com", "target": "_blank"})), {"href": "https://www.google.com", "target": "_blank"} )
        node2 = HTMLNode("<p>", "This is my value (:", (HTMLNode("<h3>", "ooooo smol node", None, {"href": "https://www.google.com", "target": "_blank"})), {"href": "https://www.google.com", "target": "_blank"} )
        print(f"EQEMPTYTAGComparing tag: {node.tag} == {node2.tag} : { node.tag == node2.tag }")
        print(f"EQEMPTAGComparing value: {node.value} == {node2.value} : {node.value == node2.value}")
        print(f"EQEMPTAGComparing children: {node.children} == {node2.children} : {node.children == node2.children}")
        print(f"EQEMPTAGComparing props: {node.props} == {node2.props} : {node.props == node2.props }")
        print(f'guy cmon wat ??????? {node.children.tag} == {node2.children.tag} : {node.children.tag == node2.children.tag}')
        print(f'guy cmon wat ??????? {node.children.value} == {node2.children.value} : {node.children.value == node2.children.value}')
        print(f'guy cmon wat ??????? {node.children.children} == {node2.children.children} : {node.children.children == node2.children.children}')
        print(f'guy cmon wat ??????? {node.children.props} == {node2.children.props} : {node.children.props== node2.children.props}')
        self.assertEqual(node, node2)
    #When props or children is None or empty.

# When attributes (e.g., tag, value, props, or children) are missing or empty.

# When the node is created with different data types, like an integer as the value or invalid data in props.


if __name__ == "__main__":
    unittest.main()
