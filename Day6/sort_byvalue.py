dct={'a': 2,  'c': 4,'d':3,'b': 1,}
print(dct)
print(sorted(dct.items()))
tmp=list()
for key,val in dct.items():
    tmp.append((val,key))
print(sorted(tmp,reverse=True))
