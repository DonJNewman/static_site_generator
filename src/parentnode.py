from htmlnode import HTMLNode
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)
        # Validate required arguments
        if not tag:
            raise ValueError("ParentNode must have a valid tag")

        if children is None:
            raise ValueError("ParentNode must have children")

        # Verify all children have a `to_html` method
        if not all(hasattr(child, "to_html") for child in children):
            raise TypeError("All children must have a `to_html` method")

        # Assign attributes
        self.tag = tag
        self.children = children
        self.props = props or {}
        self.children = children
        
    
  
    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag.")
  

        props_string = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        props_string = f" {props_string}" if props_string else ""
        if not self.children:
            return f"<{self.tag}{props_string}></{self.tag}>"
        children_html = "".join(child.to_html() for child in self.children)

        return f"<{self.tag}{props_string}>{children_html}</{self.tag}>"


#return string repping html tag of node and children
#recursion call on nested child nodes
#iterate over all children and call to html
#concatenate results and injecting 
#between opening and closing parent tags
