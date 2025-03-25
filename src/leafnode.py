from htmlnode import HTMLNode
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
        self.tag = tag
        self.value = value
        self.props = props or {} 
   
    def to_html(self):
        if not self.tag:
            return self.value if self.value is not None else None  # Return None if no value
        if self.value is None:
            return None  
       
        props_string = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        props_string = f" {props_string}" if props_string else ""
        value = self.value if self.value is not None else ""
        return f"<{self.tag}{props_string}>{value}</{self.tag}>"