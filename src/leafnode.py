from htmlnode import HTMLNode
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
        self.tag = tag
        self.value = value
        self.props = props   
   
    def to_html(self):
        if self.value == None:
            raise ValueError('missing value for leaf')
        if self.tag == None:
            return(f"{self.value}")
        if self.tag == "a":
            for key, value in self.props.items():
                prop_key = key
                prop_value = value
            return(f'<a {prop_key}="{prop_value}">{self.value}</a>')
        else:
            return(f'<{self.tag}>{self.value}</{self.tag}>')