class Node:
    count=0
    nodelist={}

    def __init__(self,v:int,l=None,r=None):
        self.v=v
        self.c1=l
        self.c2=r
        self._id=None
        self.nullable=None
        self.firstpos=set()
        self.lastpos=set()
        self.followpos=set()
        if v<1e5+2: # not operator
            Node.count+=1
            self._id=Node.count
            Node.nodelist[self._id]=self

    def __str__(self):
        return f'v={self.v} ,\nl={self.c1.v if self.c1 else None} , r={self.c2.v if self.c2 else None}\nid={self._id}'\
            f'\nnullable: {self.nullable}'\
            f'\nfpos: {self.firstpos} , lpos: {self.lastpos}'\
            f'\nflwpos: {self.followpos}'
