from .node import Node
from .operators import smb

__all__=['DfaBuilder']


class DfaBuilder:
    def __init__(self):
        self.__dtrans={} # dfa
        self.startstate=None
        self.finalstates=set()
        self.trapstate=frozenset([-1])

    def from_syntax_tree(self,tree):
        dstates=[frozenset(tree.root.firstpos)]
        vis=set()
        statename={}
        while dstates:
            state=dstates.pop()
            if state in vis: continue
            vis.add(state)
            statename.setdefault(state,f's{len(statename)}')
            if any(Node.nodelist[i].v==smb['#'] for i in state):
                self.finalstates.add(state)
            for a in tree.symbols:
                z=set()
                for i in state:
                    node=Node.nodelist[i]
                    if node.v==a:
                        z|=node.followpos
                if len(z):
                    z=frozenset(z)
                    dstates.append(z)
                    self.__dtrans.setdefault(state,{})
                    self[state][a]=z

        self.startstate='s0'
        self.finalstates={statename[i] for i in self.finalstates}
        self.__dtrans={statename[k1]:{chr(k2):statename[self[k1][k2]] for k2 in self[k1]} for k1 in self.__dtrans}

        return self

    def move(self,current,symbol):
        if current==self.trapstate:
            return self.trapstate
        try:
            return self[current][symbol]
        except KeyError:
            return self.trapstate

    def simulate(self,txt):
        current=self.startstate
        for c in txt:
            current=self.move(current,c)
        return current in self.finalstates

    @property
    def transition_table(self):
        '''return a copy of the dfa after adding all state names'''
        from copy import deepcopy
        return deepcopy(self.__dtrans)

    def __getitem__(self,state):
        return self.__dtrans[state]
