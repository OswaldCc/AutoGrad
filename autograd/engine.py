class Value:
    def __init__(self,data,_children=(),_op='',label=''):
        self.data=data
        self._prev=set(_children)
        self._op=_op
        self.label=label
    def __repr__(self):
        return f"Value(data={self.data})"
    
    def __str__(self):
        return f"{self.data}"
    def __add__(self,other):
        out=Value(self.data+other.data,(self,other),'+')
        return out 