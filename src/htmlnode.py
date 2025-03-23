class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props




    def to_html(self):
        #Child classes will override
        raise NotImplementedError
    
    def __eq__(self, other):
        return (self.tag == other.tag and 
                self.value == other.value and 
                self.children == other.children and
                self.props == other.props
                )
    
    def props_to_html(self):
        print('--------------IS THIS LINE RUNNING ? BUGS PROBABLY HERE')
        for key,value in self.props.items():

            print(f'href="{key}" target="{value}"')
       
        # Add a props_to_html(self) method. It should return
        # a string that represents the HTML attributes of the node. For example, if self.props is:

       #gonna have to think about this one for a sec, 
                                        #gotta unpack the dictionary right? cus props could have a bunch of items
                                            #soooooooooooo for every key value in items maybe


    def __repr__(HTMLNode):
        return(f'HTMLNode({HTMLNode.tag}, {HTMLNode.value}, {HTMLNode.children}, {HTMLNode.props} )')
