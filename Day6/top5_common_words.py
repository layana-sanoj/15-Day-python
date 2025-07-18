file=input('enter the file name: ')
try:
    fhand=open(file)
except:
    print('FILE NOT FOUND')
    exit()             

counts=dict()
for line in fhand:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

tmp=list()
for key,val in counts.items():
    tmp.append((val,key))

tmp=tmp.sorted(tmp,reverse=True)
for val,key in tmp[:5]:
    print(key, val)
