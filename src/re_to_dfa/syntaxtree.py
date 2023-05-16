from .node import Node
from .operators import op,smb

__all__ = ['SyntaxTree']


class SyntaxTree:
    def __init__(self,postfixRegex):
        self.__z=reversed(postfixRegex)
        self.root=Node(next(self.__z))
        self.symbols=set(i for i in postfixRegex if i<1e5+2 and i!=smb['$'])
        self.__generate(self.root)

    def __generate(self,rt:Node): # dfs
        if rt.v==op['*']:
            rt.c1=Node(next(self.__z))
            self.__generate(rt.c1)
        elif rt.v>1e5+1: # operator
            rt.c2=Node(next(self.__z))
            self.__generate(rt.c2)
            rt.c1=Node(next(self.__z))
            self.__generate(rt.c1)
        rt.nullable=calcNullable(rt)
        rt.firstpos=calcFirstpos(rt)
        rt.lastpos=calcLastpos(rt)
        calcFollowpos(rt)


def calcNullable(n:Node):
    if n is None:
        return False
    if n.c1==n.c2==None: #leaf node
        if n.v==smb['$']: # epsilon
            return True
        if n._id:
            return False
    if n.v==op['|']:
        return calcNullable(n.c1) or calcNullable(n.c2)
    if n.v==op['.']:
        return calcNullable(n.c1) and calcNullable(n.c2)
    if n.v==op['*']:
        return True


def calcFirstpos(n:Node):
    if n.c1==n.c2==None:
        if n.v==smb['$']: # epsilon
            return set() #emptyset
        if n._id:
            return {n._id}
    if n.v==op['|']:
        return n.c1.firstpos | n.c2.firstpos
    if n.v==op['.']:
        return n.c1.firstpos | (n.c2.firstpos if n.c1.nullable else set())
    if n.v==op['*']:
        return n.c1.firstpos

def calcLastpos(n:Node):
    if n.c1==n.c2==None:
        if n.v==smb['$']: # epsilon
            return set()
        if n._id:
            return {n._id}
    if n.v==op['|']:
        return n.c1.lastpos | n.c2.lastpos
    if n.v==op['.']:
        return n.c2.lastpos | (n.c1.lastpos if n.c2.nullable else set())
    if n.v==op['*']:
        return n.c1.lastpos


def calcFollowpos(n:Node):
    if n.v==op['.']:
        for i in n.c1.lastpos:
            Node.nodelist[i].followpos |= n.c2.firstpos
    if n.v==op['*']:
        for i in n.lastpos:
            Node.nodelist[i].followpos |= n.firstpos
