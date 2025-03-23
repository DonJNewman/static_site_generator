from htmlnode import HTMLNode
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
        self.tag = tag
        self.value = value
        self.props = props
        
    # def make_end_tag (self):
    #     split_tag=self.tag.split()
    #     split_tag.insert(1, "/")
    #     return "".join(split_tag)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return(f"{self.value}")
        if self.tag == "<a>":
            return(f'<a {self.props}>{self.value}</a>')
        else:
            return(f'<{self.tag}>{self.value}</{self.tag}>')


# Create a child class of HTMLNode called LeafNode. Its constructor should differ slightly from the HTMLNode class because:

# It should not allow for any children
# The value data member should be required (and tag even though the tag's value may be None)
# Use the super() function to call the constructor of the HTMLNode class.


# LeafNode("p", "This is a paragraph of text.").to_html()
# "<p>This is a paragraph of text.</p>"

# LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
# "<a href="https://www.google.com">Click me!</a>"

# If the leaf node has no value, it should raise a ValueError. All leaf nodes must have a value.
# If there is no tag (e.g. it's None), the value should be returned as raw text.
# Otherwise, it should render an HTML tag. For example, these leaf nodes: