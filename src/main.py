from re_to_dfa import *

# simple regex
dfa = re_to_dfa('\.\+#')
print(dfa.simulate('.+#'))
print(dfa.transition_table)
print(dfa.startstate,dfa.finalstates,sep=' <-> ',end='\n\n')

# variable assignment
regex='\s*(((int)|(long)|(double)|(float)|(string))\s+)(\s*\w+\s*(=\s*(\d+|("(\w|\s|\d)+"))\s*)?,?)*\s*;\s*'
dfa=re_to_dfa(regex)
print(dfa.simulate('float d, e;')) # true
print(dfa.simulate('string x="hello world";')) # true
print(dfa.simulate('a=10;')) # false
print(dfa.simulate('int a=10;')) # true

print()

regex2 = '.*\d+.*' # number anywhere in string
dfa2= re_to_dfa(regex2)
print(dfa2.simulate('Replace 123 with any number here'))
