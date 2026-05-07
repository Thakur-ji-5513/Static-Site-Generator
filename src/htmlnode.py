class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None or self.props == {}:
            return ""
        else:
            ans = ""
            for key, value in self.props.items():
                new = f' {key}="{value}"'
                ans = ans+new
            return ans

    def __repr__(self):
        return f'tag = {self.tag} \n value = {self.value}\n children = {self.children}\n props = {self.props}\n'


class LeafNode(HTMLNode):
    def __init__(self, tag , value , props = None ):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        else:
            if self.props is None:
                return f'<{self.tag}>{self.value}</{self.tag}>'  
            else: 
                ans = f'<{self.tag}'
                for key in self.props:
                    ans = ans + f' {key}="{self.props[key]}"'
                return f'{ans}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f'tag = {self.tag} \n value = {self.value}\n props = {self.props}\n'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError
        elif self.children is None:
            raise ValueError("children missing!")
        else:
            final = f"<{self.tag}{self.props_to_html()}>"
            for leaf in self.children:
                final = final + leaf.to_html()
            return final + f'</{self.tag}>'

