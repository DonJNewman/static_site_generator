from htmlnode import HTMLNode
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    
    def to_html(self):
        probably_need_this = []
        if self.tag == None:
            raise ValueError(f'Missing Tag for parent {self}')
        if self.value == None:
            raise ValueError(f'Missing value for parent {self}')
        for child in self.children:
            temp = self.to_html()
            probably_need_this.append(temp)
        final_string = "".join(probably_need_this)

        print(final_string)
        return final_string    
            


#return string repping html tag of node and children
#recursion call on nested child nodes
#iterate over all children and call to html
#concatenate results and injecting 
#between opening and closing parent tags
