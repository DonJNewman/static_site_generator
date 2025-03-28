from enum import Enum
from leafnode import LeafNode
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE =  "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type 
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text and 
                self.text_type == other.text_type and 
                self.url == other.url)
    def __repr__(TextNode):
        return(f'TextNode({TextNode.text}, {TextNode.text_type}, {TextNode.url} )')


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text, text_node.url)
        
    elif text_node.text_type== TextType.TEXT:
        return LeafNode("b", text_node.text)
    elif text_node.text_type== TextType.TEXT:
        return  LeafNode("i", text_node.text)
    elif text_node.text_type.CODE== TextType.TEXT:
        return  LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a",text_node.text, text_node.url)
    elif text_node.text_type == TextType.IMAGE:
         props = {"src": text_node.url, "alt": text_node.text}
         return LeafNode("img", "", props)
   
    else:
        raise Exception('Invalid text type') 