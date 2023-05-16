__all__=['smb','op','opsmb']

smb={x:int(1e5)+i for i,x in enumerate('$#()[]')} # custom symbols
op={x:int(1.1e5)+i for i,x in enumerate('+?.|*')} # operators
opsmb={**op,**smb} # operators + symbols
