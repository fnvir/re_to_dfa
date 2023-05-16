__all__=['re_to_dfa']

from .utils import infix_to_postfix,add_concat,supercharge,regex_toStr
from .syntaxtree import SyntaxTree
from .dfa import DfaBuilder


def re_to_dfa(regex):
    rgx=infix_to_postfix(add_concat(supercharge(regex)))
    tree=SyntaxTree(rgx)
    return DfaBuilder().from_syntax_tree(tree)
